"""Popula o banco com o conteúdo institucional descrito no README.

Como o arquivo db.sqlite3 não vai para o repositório, esta migration garante
que qualquer pessoa da equipe tenha o site completo logo após rodar o comando
migrate. O conteúdo pode ser editado depois pelo admin do Django.
"""
from django.db import migrations

MEMBROS = [
    ('Arthur Freitas Sultanum Burgos', 'afsb2@cesar.school'),
    ('Bruna Rocha Souto Walter', 'brsw@cesar.school'),
    ('Julia Farias Amancio', 'jfa@cesar.school'),
    ('Luiz Eduardo da Silva Moreira', 'lesm@cesar.school'),
    ('Miguel Magalhães Drechsler', 'mmd3@cesar.school'),
    ('Thiago Henrique Sousa do Monte', 'thsm@cesar.school'),
]

PILARES = [
    ('E', 'Ambiental',
     'Consumo de recursos, resíduos, energia e as escolhas do dia a dia que '
     'reduzem o impacto da operação.'),
    ('S', 'Social',
     'Relação com pessoas, fornecedores e comunidade, incluindo condições de '
     'trabalho e diversidade.'),
    ('G', 'Governança',
     'Transparência, ética e a forma como as decisões são tomadas e '
     'registradas dentro da empresa.'),
]

OBJETIVOS = [
    'Compreender melhor os pilares ESG (Ambiental, Social e Governança).',
    'Organizar práticas sustentáveis no dia a dia da gestão.',
    'Acompanhar a evolução por meio de critérios objetivos.',
    'Identificar oportunidades de melhoria contínua.',
    'Fortalecer o posicionamento de marca e a responsabilidade social.',
]

PRATICAS_FDS = [
    'Levantamento e refinamento de requisitos.',
    'Modelagem de solução orientada a problema real.',
    'Desenvolvimento incremental de funcionalidades.',
    'Organização do trabalho em sprints.',
    'Colaboração em equipe e versionamento de código.',
    'Validação contínua e documentação técnica.',
]

TECNOLOGIAS = [
    ('Python', 'Linguagem principal usada no back-end da plataforma.'),
    ('Django', 'Framework web que estrutura o sistema e suas páginas.'),
    ('SQL', 'Modelagem, armazenamento e consulta dos dados.'),
    ('VS Code', 'Ambiente de desenvolvimento adotado pela equipe.'),
]

SECOES = [
    ('index', 'A metáfora da tatuagem',
     'Usamos a tatuagem como imagem central do projeto porque ela representa '
     'identidade, compromisso e permanência. Assim como uma tatuagem carrega '
     'significado duradouro, a sustentabilidade também deve ser incorporada à '
     'cultura da organização de forma autêntica e consistente. ESG não deve '
     'ser tratado apenas como tendência, mas como parte da estratégia da '
     'empresa no longo prazo.'),
    ('quem_somos', 'O que nos move',
     'Muitas empresas reconhecem a importância do ESG, mas ainda encontram '
     'dificuldades para transformar esse conceito em ações concretas dentro '
     'da rotina do negócio. Nosso trabalho parte dessa lacuna. Construímos o '
     'ESGRise para ampliar a percepção de valor dessas práticas e apoiar a '
     'tomada de decisão com base em dados, organização de processos e '
     'acompanhamento contínuo de metas sustentáveis.'),
    ('quem_somos', 'Como trabalhamos',
     'Organizamos o trabalho em sprints, com entregas incrementais, '
     'colaboração em equipe, versionamento de código e validação contínua '
     'junto ao problema real. A documentação técnica acompanha cada etapa do '
     'desenvolvimento.'),
    ('sobre_projeto', 'Descrição do projeto',
     'O ESGRise é um projeto acadêmico desenvolvido na disciplina de '
     'Fundamentos de Desenvolvimento de Software, com foco em criar uma '
     'solução que aproxime ESG, sustentabilidade e gestão empresarial da '
     'realidade das PMEs. Muitas empresas reconhecem a importância do ESG, '
     'mas encontram dificuldades para transformar esse conceito em ações '
     'concretas. O ESGRise busca ampliar a percepção de valor dessas '
     'práticas e apoiar a tomada de decisão com base em dados.'),
    ('sobre_projeto', 'Impacto acadêmico',
     'Consolidar os aprendizados de FDS por meio de um projeto completo, com '
     'problema real, planejamento, implementação e documentação.'),
    ('sobre_projeto', 'Impacto social e de mercado',
     'Apoiar PMEs na adoção de uma gestão mais sustentável e estratégica, '
     'mostrando que ESG pode ser acessível, mensurável e vantajoso para '
     'negócios de diferentes portes.'),
    ('sobre_projeto', 'Síntese',
     'O ESGRise propõe uma plataforma que transforma conceitos de ESG em '
     'práticas de gestão aplicáveis ao contexto das PMEs, unindo propósito, '
     'inovação e organização técnica para construir uma solução relevante, '
     'educativa e de valor duradouro.'),
]

def carregar_conteudo(apps, schema_editor):
    MembroEquipe = apps.get_model('forum', 'MembroEquipe')
    Pilar = apps.get_model('forum', 'Pilar')
    ItemLista = apps.get_model('forum', 'ItemLista')
    Tecnologia = apps.get_model('forum', 'Tecnologia')
    SecaoConteudo = apps.get_model('forum', 'SecaoConteudo')

    for ordem, (nome, email) in enumerate(MEMBROS, start=1):
        MembroEquipe.objects.create(nome=nome, email=email, ordem=ordem)

    for ordem, (sigla, nome, descricao) in enumerate(PILARES, start=1):
        Pilar.objects.create(sigla=sigla, nome=nome, descricao=descricao,
                             ordem=ordem)

    for ordem, texto in enumerate(OBJETIVOS, start=1):
        ItemLista.objects.create(categoria='objetivo', texto=texto,
                                 ordem=ordem)

    for ordem, texto in enumerate(PRATICAS_FDS, start=1):
        ItemLista.objects.create(categoria='pratica_fds', texto=texto,
                                 ordem=ordem)

    for ordem, (nome, descricao) in enumerate(TECNOLOGIAS, start=1):
        Tecnologia.objects.create(nome=nome, descricao=descricao, ordem=ordem)

    for ordem, (pagina, titulo, texto) in enumerate(SECOES, start=1):
        SecaoConteudo.objects.create(pagina=pagina, titulo=titulo,
                                     texto=texto, ordem=ordem)


def remover_conteudo(apps, schema_editor):
    for nome_model in ['MembroEquipe', 'Pilar', 'ItemLista', 'Tecnologia',
                       'SecaoConteudo']:
        apps.get_model('forum', nome_model).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(carregar_conteudo, remover_conteudo),
    ]
