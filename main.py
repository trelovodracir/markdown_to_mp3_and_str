"""
Este código demonstra a geração de legendas e audío a partir
de um arquivo markdown, incluindo:
- Estilo de código com PEP 8
"""

import subprocess
import os
from datetime import datetime


def audio_and_sub(input_dir, output_dir, md_file, voice, rate):
    """
    Converte um arquivo Markdown para áudio usando edge-tts e gera legendas.

    Args:
        input_dir (str): Diretório do arquivo Markdown.
        output_dir (str): Diretório onde o áudio e as legendas serão salvos.
        md_file (str): Nome do arquivo Markdown (.md).
        voice (str): Voz TTS a ser utilizada (padrão: pt-BR-FranciscaNeural).
        rate (str): Velocidade da fala (exemplo: +20% ou -10%).
    """
    # Caminho completo do arquivo Markdown
    md_path = os.path.join(input_dir, md_file)

    # Verifica se o arquivo existe
    if not os.path.isfile(md_path):
        print(f"Arquivo Markdown não encontrado: {md_path}")
        return

    # Lê o conteúdo do arquivo Markdown
    with open(md_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Remove possíveis tags Markdown (opcional, se desejar limpar o texto)
    text = text.replace("#", "").replace("*", "").replace("`", "").strip()

    # Cria o nome do arquivo de saída com base na data e hora
    timestamp = datetime.now().strftime("%b_%d_%Y_%H-%M")
    base_filename = f"note_-_{timestamp}"
    audio_output_path = os.path.join(output_dir, f"{base_filename}.mp3")
    subtitle_output_path = os.path.join(output_dir, f"{base_filename}.srt")

    # Comando do edge-tts para gerar áudio e legendas
    cmd = [
        "edge-tts",
        "--text", text,
        "--write-media", audio_output_path,
        "--write-subtitles", subtitle_output_path,
        "--rate", rate,
        "--voice", voice
    ]

    # Executa o comando no terminal
    try:
        subprocess.run(cmd, check=True)
        print(f"Áudio gerado com sucesso: {audio_output_path}")
        print(f"Legendas geradas com sucesso: {subtitle_output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar edge-tts: {e}")


# Diretórios e arquivo Markdown
input_directory = "./model/input"
output_directory = "./model/output"
markdown_file = "machado_de_assis.md"
model = "pt-BR-FranciscaNeural"
speed = "+30%"

# Chamada da função
audio_and_sub(input_directory, output_directory, markdown_file, model, speed)
