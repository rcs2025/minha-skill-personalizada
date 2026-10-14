import os
from PIL import Image, ImageDraw, ImageFont

# Especificações de Formato / Resolução por Plataforma
FORMATS = {
    "instagram_post": {"width": 1080, "height": 1080, "ratio": "1:1"},
    "instagram_reels": {"width": 1080, "height": 1920, "ratio": "9:16"},
    "youtube_thumbnail": {"width": 1280, "height": 720, "ratio": "16:9"},
    "youtube_shorts": {"width": 1080, "height": 1920, "ratio": "9:16"}
}

def create_template_image(platform_type: str, title_text: str, output_path: str = "output.png"):
    """
    Gera uma imagem base com a resolução correta para a plataforma escolhida.
    """
    if platform_type not in FORMATS:
        raise ValueError(f"Plataforma inválida. Escolha entre: {list(FORMATS.keys())}")
    
    spec = FORMATS[platform_type]
    width, height = spec["width"], spec["height"]
    
    # Criar imagem base
    image = Image.new("RGB", (width, height), color=(20, 20, 30))
    draw = ImageDraw.Draw(image)
    
    # Adicionar texto centralizado
    text_to_display = f"[{platform_type.upper()}]\n{title_text}"
    draw.text((width // 10, height // 2), text_to_display, fill=(255, 255, 255))
    
    image.save(output_path)
    print(f"✅ Imagem gerada com sucesso para {platform_type} ({width}x{height}px): {output_path}")

if __name__ == "__main__":
    # Exemplo de uso:
    create_template_image("instagram_reels", "Dicas de Produtividade", "reels_capa.png")
    create_template_image("youtube_thumbnail", "Como Criar uma Skill no GitHub", "thumb_yt.png")
