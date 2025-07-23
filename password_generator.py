
import random  # Importa o módulo random para geração de números aleatórios
import string  # Importa o módulo string para acessar conjuntos de caracteres

def generate_password(length=12, include_numbers=True, include_special=True, 
                     uppercase=True, lowercase=True): # Define a função para gerar a senha
    caracteres = ''  # Inicializa a string de caracteres permitidos
    if lowercase:
        caracteres += string.ascii_lowercase  # Adiciona letras minúsculas se permitido
    if uppercase:
        caracteres += string.ascii_uppercase  # Adiciona letras maiúsculas se permitido
    if include_numbers:
        caracteres += string.digits  # Adiciona números se permitido
    if include_special:
        caracteres += '!@#$%&*+-=?_'  # Adiciona caracteres especiais se permitido

    if not caracteres:
        print('Erro: selecione pelo menos um tipo de caractere!')  # Garante que pelo menos um tipo foi selecionado
        return None

    senha = ''  # Inicializa a senha como string vazia
    for _ in range(length):
        senha += random.choice(caracteres)  # Escolhe um caractere aleatório da string de caracteres permitidos e adiciona à senha.

    return senha  # Retorna a senha gerada


def interactive_mode():
    print('Gerador de Senhas Simples')  # Título do programa
    print('-' * 25)
    try:
        # Coleta as preferências do usuário para a senha
        length = int(input('Quantos caracteres? (padrão 12): ') or '12')  # Pergunta o tamanho da senha
        usar_maiusculas = input('Incluir letras maiúsculas? (S/n): ').strip().lower() != 'n'  # Pergunta sobre maiúsculas
        usar_minusculas = input('Incluir letras minúsculas? (S/n): ').strip().lower() != 'n'  # Pergunta sobre minúsculas
        usar_numeros = input('Incluir números? (S/n): ').strip().lower() != 'n'  # Pergunta sobre números
        usar_especiais = input('Incluir caracteres especiais (!@#$%&*+-=?_)? (S/n): ').strip().lower() != 'n'  # Pergunta sobre especiais

        # Garante que pelo menos um tipo de caractere foi selecionado
        if not any([usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais]):
            print('Erro: selecione pelo menos um tipo de caractere!')
            return

        # Gera a senha com as opções escolhidas
        senha = generate_password(
            length=length,
            include_numbers=usar_numeros,
            include_special=usar_especiais,
            uppercase=usar_maiusculas,
            lowercase=usar_minusculas
        )
        print('\nSenha gerada:')  # Exibe a senha gerada
        print(senha)
    except Exception as e:
        print('Erro:', e)  # Exibe mensagem de erro caso ocorra


def main():
    interactive_mode()  # Função principal que inicia o modo interativo

if __name__ == "__main__":
    main()  # Executa o programa se for chamado diretamente
