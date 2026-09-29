import os
import sys
try:
    from PIL import Image
except ImportError:
    os.system('pip install Pillow')
    from PIL import Image

image_dir = r"e:\Downloads\meera-radhey saloon\images"
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        file_path = os.path.join(image_dir, filename)
        
        # Get base name correctly, removing multiple extensions like .jpg.jpg
        base_name = filename.split('.')[0]
        out_path = os.path.join(image_dir, f"{base_name}.webp")
        
        try:
            with Image.open(file_path) as img:
                # Convert to RGB to be safe
                img = img.convert('RGB')
                
                # Resize if it's too large (max 1920x1080 bounding box)
                img.thumbnail((1920, 1920), Image.Resampling.LANCZOS)
                
                # Save as webp with 80% quality
                img.save(out_path, 'webp', quality=75, method=6)
                print(f"✅ Converted: {filename} -> {base_name}.webp")
        except Exception as e:
            print(f"❌ Failed to convert {filename}: {e}")
