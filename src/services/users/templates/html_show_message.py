def send_template_change_password(code: str):
    template_show_message = f"""<!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recuperação de Acesso - IdeiaFlow</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                padding: 20px 0;
                background-color: #ff8c42;
                color: #ffffff;
                border-radius: 8px 8px 0 0;
            }}
            .header h1 {{
                margin: 0;
                font-size: 24px;
                font-weight: bold;
            }}
            .content {{
                padding: 20px;
                text-align: center;
            }}
            .content p {{
                font-size: 16px;
                line-height: 1.6;
                color: #555;
            }}
            .code {{
                font-size: 28px;
                font-weight: bold;
                color: #ff8c42;
                letter-spacing: 2px;
                margin: 20px 0;
            }}
            .button {{
                display: inline-block;
                padding: 12px 24px;
                margin: 20px 0;
                font-size: 16px;
                color: #ffffff;
                background-color: #ff8c42;
                text-decoration: none;
                border-radius: 5px;
            }}
            .button:hover {{
                background-color: #ff6e1a;
            }}
            .footer {{
                font-size: 12px;
                color: #888;
                text-align: center;
                margin-top: 20px;
                border-top: 1px solid #eeeeee;
                padding-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Recuperação de Acesso - IdeiaFlow</h1>
            </div>
            <div class="content">
                <p>Olá,</p>
                <p>Recebemos uma solicitação para redefinir sua senha no <strong>IdeiaFlow</strong>, o seu app de blocos de notas e ideias.</p>
                <p>Use o código abaixo para recuperar o acesso:</p>
                <div class="code">{code}</div>
                <p>Se não foi você que solicitou, por favor ignore esta mensagem.</p>
            </div>
            <div class="footer">
                <p>© 2024 IdeiaFlow. Todos os direitos reservados.</p>
            </div>
        </div>
    </body>
    </html>"""

    return template_show_message
