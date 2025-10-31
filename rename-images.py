#!/usr/bin/env python3
"""
Script to read quote graphics and rename them based on the text content.
Uses OCR to extract text and creates dash-cased filenames.
"""

import os
import re
from pathlib import Path
from PIL import Image
import pytesseract

def text_to_dash_case(text):
    """Convert text to dash-case filename."""
    # Remove special characters and convert to lowercase
    text = text.lower()
    # Remove @TruthOverTactic and similar branding
    text = re.sub(r'@\w+', '', text)
    # Remove punctuation except spaces
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with dashes
    text = re.sub(r'\s+', '-', text.strip())
    # Remove multiple consecutive dashes
    text = re.sub(r'-+', '-', text)
    # Limit length to reasonable filename size (max 100 chars)
    if len(text) > 100:
        text = text[:100].rsplit('-', 1)[0]
    return text

def extract_text_from_image(image_path):
    """Extract text from image using OCR."""
    try:
        img = Image.open(image_path)
        # Extract text using tesseract
        text = pytesseract.image_to_string(img)
        # Clean up the text
        text = text.strip()
        # Remove the @TruthOverTactic branding
        text = re.sub(r'@TruthOverTactic', '', text, flags=re.IGNORECASE)
        text = text.strip()
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def rename_images(source_dir):
    """Rename all PNG images in the directory based on their text content."""
    source_path = Path(source_dir)

    if not source_path.exists():
        print(f"Directory not found: {source_dir}")
        return

    # Get all PNG files
    png_files = sorted(source_path.glob("*.png"))

    print(f"Found {len(png_files)} PNG files to process\n")

    renamed_count = 0
    errors = []

    for img_file in png_files:
        print(f"Processing: {img_file.name}")

        # Extract text from image
        quote_text = extract_text_from_image(img_file)

        if not quote_text:
            errors.append(f"Could not extract text from: {img_file.name}")
            continue

        # Convert to dash-case
        new_name = text_to_dash_case(quote_text)

        if not new_name:
            errors.append(f"Could not create filename from text: {quote_text[:50]}")
            continue

        # Create new filename
        new_filename = f"{new_name}.png"
        new_path = img_file.parent / new_filename

        # Check if file already exists
        if new_path.exists() and new_path != img_file:
            # Add number suffix if duplicate
            counter = 2
            while new_path.exists():
                new_filename = f"{new_name}-{counter}.png"
                new_path = img_file.parent / new_filename
                counter += 1

        # Rename the file
        try:
            img_file.rename(new_path)
            print(f"  → Renamed to: {new_filename}\n")
            renamed_count += 1
        except Exception as e:
            errors.append(f"Error renaming {img_file.name}: {e}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Successfully renamed: {renamed_count} files")
    print(f"  Errors: {len(errors)}")

    if errors:
        print(f"\nErrors encountered:")
        for error in errors:
            print(f"  - {error}")

if __name__ == "__main__":
    source_directory = "/Volumes/Development/narcissist-book/social/images/raw"
    rename_images(source_directory)
