
from PIL import Image
from transformers import AutoModelForCausalLM
import torch

model_name = "starvector/starvector-1b-im2svg"

# Load model on CPU
starvector = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    torch_dtype=torch.float32
).to("cpu")
starvector.eval()

# Access processor and tokenizer
processor = starvector.model.processor
tokenizer = starvector.model.svg_transformer.tokenizer

def image_to_svg(image_path: str) -> str:
    image_pil = Image.open(image_path).convert("RGB")
    image = processor(image_pil, return_tensors="pt")['pixel_values']

    batch = {"image": image}

    with torch.no_grad():
        raw_svg = starvector.generate_im2svg(batch, max_length=4000)[0]

    return raw_svg.strip()
