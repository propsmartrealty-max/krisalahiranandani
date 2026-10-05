#!/usr/bin/env python3
"""
Generates complete suite of high-fidelity, multi-resolution site favicons
from the user-provided Hiranandani official brand asset.
"""

import os
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
SOURCE_IMAGE = "/Users/vikasyewle/.gemini/antigravity/brain/171ccd21-6de4-468c-ad7d-745c9459b56d/.user_uploaded/media_1791183933712.png"

def create_square_canvas(img, target_size, padding_ratio=0.06):
    """
    Crops image to non-transparent bounding box and places it centered
    on a square canvas with specified padding ratio.
    """
    bbox = img.getbbox()
    cropped = img.crop(bbox)
    cw, ch = cropped.size
    
    pad = int(target_size * padding_ratio)
    inner_size = target_size - (2 * pad)
    
    scale = min(inner_size / cw, inner_size / ch)
    new_w = max(1, int(cw * scale))
    new_h = max(1, int(ch * scale))
    
    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    canvas = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
    paste_x = (target_size - new_w) // 2
    paste_y = (target_size - new_h) // 2
    canvas.paste(resized, (paste_x, paste_y), resized)
    return canvas

def main():
    print(f"Loading source favicon asset from: {SOURCE_IMAGE}")
    src_img = Image.open(SOURCE_IMAGE).convert("RGBA")
    print(f"Source size: {src_img.size}, mode: {src_img.mode}")

    # 1. Master 512x512 canvas
    master_512 = create_square_canvas(src_img, 512, padding_ratio=0.06)
    
    # 2. Save favicon-512.png
    p512_path = os.path.join(PROJECT_DIR, "favicon-512.png")
    master_512.save(p512_path, "PNG", optimize=True)
    print(f"✓ Saved {p512_path}")

    # 3. Save favicon-192.png (PWA / Android standard)
    master_192 = create_square_canvas(src_img, 192, padding_ratio=0.06)
    p192_path = os.path.join(PROJECT_DIR, "favicon-192.png")
    master_192.save(p192_path, "PNG", optimize=True)
    print(f"✓ Saved {p192_path}")

    # 4. Save apple-touch-icon.png (180x180 iOS standard)
    apple_180 = create_square_canvas(src_img, 180, padding_ratio=0.06)
    apple_path = os.path.join(PROJECT_DIR, "apple-touch-icon.png")
    apple_180.save(apple_path, "PNG", optimize=True)
    print(f"✓ Saved {apple_path}")

    # 5. Save favicon-48x48.png (Google Search standard)
    f48 = create_square_canvas(src_img, 48, padding_ratio=0.04)
    f48_path = os.path.join(PROJECT_DIR, "favicon-48x48.png")
    f48.save(f48_path, "PNG", optimize=True)
    print(f"✓ Saved {f48_path}")

    # 6. Save standard favicon.png (32x32 root icon)
    f32 = create_square_canvas(src_img, 32, padding_ratio=0.04)
    f32_path = os.path.join(PROJECT_DIR, "favicon.png")
    f32.save(f32_path, "PNG", optimize=True)
    print(f"✓ Saved {f32_path}")

    # 7. Multi-resolution favicon.ico
    # Windows/Browsers standard containing 16, 32, 48, 64, 128, 256
    ico_path = os.path.join(PROJECT_DIR, "favicon.ico")
    f16 = create_square_canvas(src_img, 16, padding_ratio=0.02)
    f64 = create_square_canvas(src_img, 64, padding_ratio=0.04)
    f128 = create_square_canvas(src_img, 128, padding_ratio=0.05)
    f256 = create_square_canvas(src_img, 256, padding_ratio=0.06)
    
    master_512.save(
        ico_path,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    )
    print(f"✓ Saved multi-resolution {ico_path}")

    # Also update public/ directory copies if public/ exists
    pub_dir = os.path.join(PROJECT_DIR, "public")
    if os.path.exists(pub_dir):
        f32.save(os.path.join(pub_dir, "favicon.png"), "PNG", optimize=True)
        master_512.save(os.path.join(pub_dir, "favicon.ico"), format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
        print("✓ Mirrored favicons to public/ directory")

    print("\nAll favicon formats generated successfully!")

if __name__ == "__main__":
    main()
