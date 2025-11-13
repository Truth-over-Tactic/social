# Image Renaming Process

## Overview
This directory contains quote graphics for social media, renamed from bulk export filenames to descriptive, dash-cased names based on their quote text.

## Process Used

### 1. Visual Image Review
All images were reviewed individually to read the quote text (ignoring the @TruthOverTactic watermark present on every image).

### 2. Filename Convention
- **Format**: dash-case (all lowercase, words separated by hyphens)
- **Source**: The actual quote text on the image
- **Example**: "You're not broken. You're traumatized." → `youre-not-broken-youre-traumatized.png`

### 3. Handling Duplicates
When multiple images contained the same or very similar quotes:
- Added numerical suffix: `-2`, `-3`, etc.
- Examples:
  - `real-love-doesnt-hurt.png`
  - `real-love-doesnt-hurt-2.png`

### 4. Automation Script
Created `/Volumes/Development/narcissist-book/social/images/rename-images.sh` to execute all renames at once.

## Reusing This Pattern for Future Batches

### Step 1: Review Images
```bash
cd /path/to/new/images
ls *.png
```

### Step 2: Read Quote Text
Use Claude Code's `Read` tool to visually inspect each image and catalog the quote text.

### Step 3: Create Rename Script
```bash
#!/bin/bash

cd "/path/to/images" || exit

echo "Renaming images based on quote text..."

# Pattern: mv "original-filename.png" "dash-cased-quote-text.png"
mv "1_(Bulk X) Filename.png" "actual-quote-text-from-image.png"
mv "2_(Bulk X) Filename.png" "another-quote-text.png"
# ... continue for all images

echo "✓ All images renamed successfully!"
```

### Step 4: Execute
```bash
chmod +x rename-images.sh
./rename-images.sh
```

### Step 5: Verify
```bash
ls -1 | head -20  # View first 20 renamed files
ls | wc -l        # Count total files
```

## Best Practices

1. **Preserve Punctuation Logic**:
   - Remove apostrophes: "you're" → "youre"
   - Remove periods, commas, question marks
   - Keep meaning intact

2. **Length Considerations**:
   - Aim for 50-80 characters max
   - If quote is very long, use key words only
   - Maintain meaning and searchability

3. **Consistency**:
   - All lowercase
   - Hyphens only (no underscores or spaces)
   - No special characters except hyphens

4. **Backup First**:
   ```bash
   cp -r raw/ raw-backup/
   ```

## Current Image Count
**Total Images**: 58 quote graphics (verified)

## File Location
- **Raw Images**: `/Volumes/Development/narcissist-book/social/images/raw/`
- **Rename Script**: `/Volumes/Development/narcissist-book/social/images/rename-images.sh`

## Quote Themes Represented
All images contain quotes from Chapters 1-4 across three voice tones:
- **Empowered** (confident, strong, survivor-focused)
- **Empathetic** (validating, understanding, trauma-informed)
- **Frustrated/Angry** (acknowledging justified anger at injustice)

## Next Steps for Future Batches

1. Export new batch from Canva with bulk naming
2. Place in staging directory
3. Use Claude Code to read all images
4. Create new rename script based on this pattern
5. Execute and verify
6. Move to production directory

---

*Last Updated: 2025-10-31*
*Processed: 58 images from Chapters 1-4*
