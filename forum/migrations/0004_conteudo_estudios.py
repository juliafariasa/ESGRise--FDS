"""Carrega o conteúdo da tela inicial sobre ESG em estúdios de tatuagem."""
from django.db import migrations

SECOES_INDEX = [
    (1, 'Por que ESG importa para um estúdio de tatuagem',
     'Um estúdio de tatuagem é uma pequena empresa que lida todos os dias com '
     'saúde, resíduo e confiança do cliente. Diferente de um escritório, o '
     'estúdio gera resíduo perfurocortante, consome muito material '
     'descartável, guarda dados sensíveis de saúde e depende de licença da '
     'vigilância sanitária para abrir a porta. Ou seja, os três pilares do '
     'ESG já fazem parte da operação, mesmo que ninguém ali use essa sigla. '
     'Organizar essas práticas deixa de ser burocracia e vira redução de '
     'risco, de custo e de retrabalho.'),
    (2, 'Um setor pequeno, com impacto concreto',
     'A maior parte dos estúdios tem poucos profissionais e trabalha com '
     'tatuadores autônomos que alugam a cadeira. Essa estrutura enxuta '
     'costuma deixar de fora controles que empresas maiores já mantêm, como '
     'registro de procedimentos, contrato claro com quem tatua e plano de '
     'descarte de resíduos. O ESGRise existe para preencher essa lacuna com '
     'critérios simples e verificáveis, no lugar de relatórios longos que uma '
     'empresa desse porte não conseguiria manter.'),
]

PRATICAS = [
    ('E', 1, 'Descarte de perfurocortantes',
     'Agulhas, cartuchos e lâminas precisam ir para coletor rígido e ser '
     'recolhidos por empresa licenciada, com o comprovante guardado. É o item '
     'de maior risco sanitário do estúdio.'),
    ('E', 2, 'Redução de descartáveis',
     'Filme plástico, barreiras e papel toalha somam um volume alto por '
     'sessão. Trocar parte por alternativas reutilizáveis ou biodegradáveis '
     'corta custo e resíduo ao mesmo tempo.'),
    ('E', 3, 'Consumo de energia e água',
     'Autoclave, climatização e iluminação concentram a conta de luz. Medir o '
     'consumo mês a mês mostra onde dá para ajustar sem perder qualidade.'),
    ('E', 4, 'Origem das tintas e insumos',
     'Escolher tintas regularizadas e fornecedores que informam composição e '
     'lote reduz risco para o cliente e para quem tatua.'),
    ('S', 1, 'Biossegurança da equipe e do cliente',
     'Esterilização, uso correto de luvas, vacinação contra hepatite B e '
     'treinamento periódico protegem tanto o tatuador quanto quem senta na '
     'cadeira.'),
    ('S', 2, 'Relação com quem tatua no espaço',
     'Contrato escrito com o tatuador autônomo, com regras de divisão, '
     'horário e uso do estúdio, evita conflito e informalidade.'),
    ('S', 3, 'Acolhimento do cliente',
     'Atendimento preparado para pele negra, cobertura de cicatriz e público '
     'LGBTQIA+ amplia o alcance do estúdio e melhora a experiência.'),
    ('S', 4, 'Formação de novos profissionais',
     'Ensinar aprendizes com critério técnico mantém a qualidade do setor e '
     'cria sucessão dentro do próprio estúdio.'),
    ('G', 1, 'Licença sanitária em dia',
     'O alvará da vigilância sanitária é condição para funcionar. Acompanhar '
     'prazos de renovação evita interdição e multa.'),
    ('G', 2, 'Termo de consentimento e ficha do cliente',
     'Registrar histórico de saúde, alergias e o procedimento realizado '
     'protege o estúdio caso apareça uma reclamação depois.'),
    ('G', 3, 'Proteção de dados do cliente',
     'Fotos, dados de contato e informações de saúde são dados sensíveis pela '
     'LGPD. Exigem autorização para uso e guarda cuidadosa.'),
    ('G', 4, 'Preço e regras por escrito',
     'Tabela de preço, política de retoque e regra de cancelamento definidas '
     'por escrito reduzem atrito e reclamação.'),
]

BENEFICIOS = [
    'Menos risco de interdição e de multa da vigilância sanitária.',
    'Queda no custo com material descartável, energia e retrabalho.',
    'Diferenciação diante de um público que pesquisa o estúdio antes de '
    'marcar a sessão.',
    'Resposta rápida e documentada quando um cliente relata problema.',
    'Relação mais clara e estável com os tatuadores que usam o espaço.',
]

def carregar(apps, schema_editor):
    SecaoConteudo = apps.get_model('forum', 'SecaoConteudo')
    ItemLista = apps.get_model('forum', 'ItemLista')
    Pilar = apps.get_model('forum', 'Pilar')
    PraticaEstudio = apps.get_model('forum', 'PraticaEstudio')

    SecaoConteudo.objects.filter(
        pagina='index', titulo='A metáfora da tatuagem'
    ).update(ordem=9)

    for ordem, titulo, texto in SECOES_INDEX:
        SecaoConteudo.objects.create(
            pagina='index', titulo=titulo, texto=texto, ordem=ordem
        )

    for sigla, ordem, titulo, descricao in PRATICAS:
        pilar = Pilar.objects.get(sigla=sigla)
        PraticaEstudio.objects.create(
            pilar=pilar, titulo=titulo, descricao=descricao, ordem=ordem
        )

    for ordem, texto in enumerate(BENEFICIOS, start=1):
        ItemLista.objects.create(
            categoria='beneficio', texto=texto, ordem=ordem
        )


def remover(apps, schema_editor):
    SecaoConteudo = apps.get_model('forum', 'SecaoConteudo')
    ItemLista = apps.get_model('forum', 'ItemLista')
    PraticaEstudio = apps.get_model('forum', 'PraticaEstudio')

    PraticaEstudio.objects.all().delete()
    ItemLista.objects.filter(categoria='beneficio').delete()
    SecaoConteudo.objects.filter(
        pagina='index', titulo__in=[titulo for _, titulo, _ in SECOES_INDEX]
    ).delete()
    SecaoConteudo.objects.filter(
        pagina='index', titulo='A metáfora da tatuagem'
    ).update(ordem=1)


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_itemlista_categoria_praticaestudio'),
    ]

    operations = [
        migrations.RunPython(carregar, remover),
    ]
