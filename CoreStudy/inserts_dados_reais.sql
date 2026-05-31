-- Inserts gerados a partir dos dados reais do MySQL
-- Banco: db_core_study1

SET FOREIGN_KEY_CHECKS = 0;

-- Dados da tabela tbl_categoria
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (9, 'Programação');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (10, 'Design e Experiencia do Usuario');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (11, 'Desenvolvimento Web');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (12, 'Banco de Dados');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (13, 'Inteligencia Artificial');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (14, 'Segurança da Informação');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (15, 'Gestão de Projetos');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (16, 'Marketing Digital');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (17, 'Data Science');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (18, 'Cloud Computing');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (19, 'Mobile Apps');
INSERT INTO `tbl_categoria` (`id_categoria`, `nome_categoria`) VALUES (20, 'Carreira e Produtividade');

-- Dados da tabela tbl_usuarios
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (18, 'Lucas Fernandes', 'lucas.fernandes@corestudy.com', '(11) 98888-1001', '2000-02-10', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (19, 'Ana Beatriz Souza', 'ana.souza@corestudy.com', '(21) 97777-1002', '1999-06-22', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (20, 'Pedro Henrique Lima', 'pedro.lima@corestudy.com', '(31) 96666-1003', '2002-11-05', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (21, 'Camila Rocha', 'camila.rocha@corestudy.com', '(41) 95555-1004', '2001-04-18', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (22, 'Rafael Martins', 'rafael.martins@corestudy.com', '(51) 94444-1005', '1998-09-30', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (23, 'Juliana Costa', 'juliana.costa@corestudy.com', '(61) 93333-1006', '2003-01-12', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (24, 'Bruno Almeida', 'bruno.almeida@corestudy.com', '(71) 92222-1007', '2000-12-03', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (25, 'Larissa Mendes', 'larissa.mendes@corestudy.com', '(81) 91111-1008', '2002-07-27', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (26, 'Gustavo Ribeiro', 'gustavo.ribeiro@corestudy.com', '(85) 90000-1009', '1997-03-14', '123456', '2026-05-26');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (31, 'Matheus Melo', 'matheus@gmail.com', '11766665555', '1989-08-11', '12345678', '2026-05-27');
INSERT INTO `tbl_usuarios` (`id_usuario`, `nome_usuario`, `email_usuario`, `telefone_usuario`, `dt_nasc_usuario`, `senha_usuario`, `dt_cad_usuario`) VALUES (38, 'Teste', 'teste@gmail.com', '(11) 95555-6666', '2000-06-12', '12345678', '2026-05-31');

-- Dados da tabela tbl_cursos
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (11, 'Python para Iniciantes', 'Curso introdutorio para aprender logica, sintaxe Python, funcoes e pequenos projetos praticos.', 40, 9);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (12, 'Fundamentos de UX/UI Design', 'Curso para entender pesquisa com usuarios, jornada, wireframes, prototipos e interfaces digitais.', 32, 10);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (13, 'HTML e CSS Essencial', 'Aprenda a estruturar paginas web responsivas com HTML semantico e CSS moderno.', 24, 11);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (14, 'JavaScript para Web', 'Curso pratico de JavaScript para criar paginas interativas e dinamicas.', 36, 11);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (15, 'Modelagem de Banco de Dados', 'Conceitos de entidades, relacionamentos, normalizacao e criacao de modelos relacionais.', 30, 12);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (16, 'SQL na Pratica', 'Consultas, filtros, joins, agregacoes e manipulacao de dados em bancos relacionais.', 34, 12);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (17, 'Introducao a IA', 'Fundamentos de inteligencia artificial, aprendizado de maquina e aplicacoes reais.', 28, 13);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (18, 'Machine Learning Basico', 'Treinamento, validacao e avaliacao de modelos simples de aprendizado de maquina.', 42, 13);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (19, 'Fundamentos de Cybersecurity', 'Principios de seguranca, ameacas comuns e boas praticas de protecao digital.', 26, 14);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (20, 'Seguranca em Aplicacoes Web', 'Aprenda sobre autenticacao, autorizacao, injecao SQL e protecao de sistemas web.', 38, 14);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (21, 'Scrum e Metodos Ageis', 'Organizacao de times, sprints, backlog, cerim?nias ageis e melhoria continua.', 20, 15);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (22, 'Planejamento de Projetos Digitais', 'Escopo, cronograma, riscos, stakeholders e acompanhamento de entregas digitais.', 32, 15);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (23, 'SEO para Iniciantes', 'Otimizacao de paginas para buscadores, palavras-chave e analise de resultados.', 22, 16);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (24, 'Redes Sociais para Negocios', 'Estrategia de conteudo, calendario editorial, metricas e campanhas em redes sociais.', 24, 16);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (25, 'Python para Data Science', 'Uso de Python para analisar dados, manipular tabelas e gerar visualizacoes.', 44, 17);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (26, 'Visualizacao de Dados', 'Criacao de graficos e dashboards para comunicar informacoes com clareza.', 30, 17);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (27, 'Fundamentos de AWS', 'Introducao a servicos de nuvem, computacao, armazenamento e boas praticas na AWS.', 36, 18);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (28, 'Deploy de Aplicacoes na Nuvem', 'Publique aplicacoes web usando servidores, variaveis de ambiente e bancos na nuvem.', 40, 18);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (29, 'Flutter para Iniciantes', 'Crie aplicativos mobile multiplataforma com componentes, telas e navegacao.', 38, 19);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (30, 'UX para Aplicativos Mobile', 'Pesquisa, fluxo de telas, acessibilidade e prototipacao para apps mobile.', 26, 19);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (31, 'Organizacao de Estudos', 'Tecnicas para planejar estudos, manter rotina e acompanhar progresso.', 16, 20);
INSERT INTO `tbl_cursos` (`id_curso`, `titulo_curso`, `descricao_curso`, `carga_hora_curso`, `fk_tbl_categoria_id_categoria`) VALUES (32, 'Preparacao para Entrevistas Tech', 'Curriculo, portfolio, desafios tecnicos e comunicacao em entrevistas de tecnologia.', 18, 20);

-- Dados da tabela tbl_modulos
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (6, 'Primeiros Passos com Python', 11);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (7, 'Prototipacao de Interfaces', 12);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (8, 'Modulo principal - HTML e CSS Essencial', 13);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (9, 'Modulo principal - JavaScript para Web', 14);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (10, 'Modulo principal - Modelagem de Banco de Dados', 15);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (11, 'Modulo principal - SQL na Pratica', 16);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (12, 'Modulo principal - Introducao a IA', 17);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (13, 'Modulo principal - Machine Learning Basico', 18);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (14, 'Modulo principal - Fundamentos de Cybersecurity', 19);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (15, 'Modulo principal - Seguranca em Aplicacoes Web', 20);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (16, 'Modulo principal - Scrum e Metodos Ageis', 21);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (17, 'Modulo principal - Planejamento de Projetos Digitais', 22);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (18, 'Modulo principal - SEO para Iniciantes', 23);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (19, 'Modulo principal - Redes Sociais para Negocios', 24);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (20, 'Modulo principal - Python para Data Science', 25);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (21, 'Modulo principal - Visualizacao de Dados', 26);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (22, 'Modulo principal - Fundamentos de AWS', 27);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (23, 'Modulo principal - Deploy de Aplicacoes na Nuvem', 28);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (24, 'Modulo principal - Flutter para Iniciantes', 29);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (25, 'Modulo principal - UX para Aplicativos Mobile', 30);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (26, 'Modulo principal - Organizacao de Estudos', 31);
INSERT INTO `tbl_modulos` (`id_modulo`, `titulo_modulo`, `fk_tbl_cursos_id_curso`) VALUES (27, 'Modulo principal - Preparacao para Entrevistas Tech', 32);

-- Dados da tabela tbl_aulas
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (6, 'Instalando o Python e criando o primeiro programa', 'https://www.youtube.com/watch?v=4p7axLXXBGU', 6);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (7, 'Aula introdutoria - HTML e CSS Essencial', 'https://www.youtube.com/watch?v=wWKft1MuuaM', 8);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (8, 'Aula introdutoria - JavaScript para Web', 'https://www.youtube.com/watch?v=rmNMBjse-m0', 9);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (9, 'Aula introdutoria - Modelagem de Banco de Dados', 'https://www.youtube.com/watch?v=W49AO7f93Jk&t=118s', 10);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (10, 'Aula introdutoria - SQL na Pratica', 'https://www.youtube.com/watch?v=OFLMhFuArXQ', 11);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (11, 'Aula introdutoria - Introducao a IA', 'https://www.youtube.com/watch?v=ucoFLlasfIo&list=PLBqjnKyN75dQiW0WJtvNoBESF5q8OWdge', 12);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (12, 'Aula introdutoria - Machine Learning Basico', 'https://www.youtube.com/watch?v=Fpi3DPDMDa8&list=PLwnip85KhroXnYqk_ske2o3TgnQrLbMU6', 13);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (13, 'Aula introdutoria - Fundamentos de Cybersecurity', 'https://www.youtube.com/watch?v=Gfh2bxe3hGU', 14);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (14, 'Aula introdutoria - Seguranca em Aplicacoes Web', 'https://www.youtube.com/watch?v=b-LoouXTu8w&list=PLVSNL1PHDWvT1zXtgrpOPeC15XeioXKuU', 15);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (15, 'Aula introdutoria - Scrum e Metodos Ageis', 'https://www.youtube.com/watch?v=HlmiVz0SqNQ', 16);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (16, 'Aula introdutoria - Planejamento de Projetos Digitais', 'https://www.youtube.com/watch?v=trhDHOC3xGw&list=PLnhUek92-enioRGAFZ9Vf_qfWt7rCR8vw', 17);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (17, 'Aula introdutoria - SEO para Iniciantes', 'https://www.youtube.com/watch?v=MsVbqaObPFQ&list=PLHz_AreHm4dm4pBTRvBFMpSXvEoymoa90', 18);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (18, 'Aula introdutoria - Redes Sociais para Negocios', 'https://www.youtube.com/watch?v=p_SZ7L1R2qg&list=PL3bIgPf3B5vjbJk28rdBywHCHbE1ydMRT', 19);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (19, 'Aula introdutoria - Python para Data Science', 'https://www.youtube.com/watch?v=F608hzn_ygo', 20);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (20, 'Aula introdutoria - Visualizacao de Dados', 'https://www.youtube.com/watch?v=kCMaqla6Grs&list=PLpdAy0tYrnKx9CtTmgSdzHz9YQ-C5ZNI9', 21);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (21, 'Aula introdutoria - Fundamentos de AWS', 'https://www.youtube.com/watch?v=HiBCv9DolxI&list=PLtL97Owd1gkQ0dfqGW8OtJ-155Gs67Ecz', 22);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (22, 'Aula introdutoria - Deploy de Aplicacoes na Nuvem', 'https://www.youtube.com/watch?v=zaj0IX8dQwA&list=PLwlq4XZ8aTmfHJTNreRyqCmXVWhyF5LHo', 23);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (23, 'Aula introdutoria - Flutter para Iniciantes', 'https://www.youtube.com/watch?v=2NQUjHZZ9t8&list=PLqdwHeoSjEN-9aGd-RxaS_2cyD_AKT0c_', 24);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (24, 'Aula introdutoria - UX para Aplicativos Mobile', 'https://www.youtube.com/watch?v=6aLr4-BOjSA', 25);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (25, 'Aula introdutoria - Organizacao de Estudos', 'https://www.youtube.com/watch?v=-mdRHwziNpU&list=PLfaiuyLsupZqIaydJNNHCJoEH951cXNT_', 26);
INSERT INTO `tbl_aulas` (`id_aula`, `titulo_aula`, `url_arqui_aula`, `fk_tbl_modulos_id_modulo`) VALUES (26, 'Aula introdutoria - Preparacao para Entrevistas Tech', 'https://www.youtube.com/watch?v=1VnUDlQf0So&list=PLJE0II7XilfWgJ2SkmbUtHUxHyzMEwWa-', 27);

-- Dados da tabela tbl_materiais
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (7, 'Checklist de instalacao do Python', 'PDF', '1.2 MB', 6);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (8, 'Apostila - HTML e CSS Essencial', 'PDF', '2.0 MB', 7);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (9, 'Exercicios - HTML e CSS Essencial', 'DOCX', '850 KB', 7);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (10, 'Apostila - JavaScript para Web', 'PDF', '2.0 MB', 8);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (11, 'Exercicios - JavaScript para Web', 'DOCX', '850 KB', 8);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (12, 'Apostila - Modelagem de Banco de Dados', 'PDF', '2.0 MB', 9);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (13, 'Exercicios - Modelagem de Banco de Dados', 'DOCX', '850 KB', 9);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (14, 'Apostila - SQL na Pratica', 'PDF', '2.0 MB', 10);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (15, 'Exercicios - SQL na Pratica', 'DOCX', '850 KB', 10);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (16, 'Apostila - Introducao a IA', 'PDF', '2.0 MB', 11);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (17, 'Exercicios - Introducao a IA', 'DOCX', '850 KB', 11);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (18, 'Apostila - Machine Learning Basico', 'PDF', '2.0 MB', 12);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (19, 'Exercicios - Machine Learning Basico', 'DOCX', '850 KB', 12);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (20, 'Apostila - Fundamentos de Cybersecurity', 'PDF', '2.0 MB', 13);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (21, 'Exercicios - Fundamentos de Cybersecurity', 'DOCX', '850 KB', 13);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (22, 'Apostila - Seguranca em Aplicacoes Web', 'PDF', '2.0 MB', 14);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (23, 'Exercicios - Seguranca em Aplicacoes Web', 'DOCX', '850 KB', 14);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (24, 'Apostila - Scrum e Metodos Ageis', 'PDF', '2.0 MB', 15);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (25, 'Exercicios - Scrum e Metodos Ageis', 'DOCX', '850 KB', 15);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (26, 'Apostila - Planejamento de Projetos Digitais', 'PDF', '2.0 MB', 16);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (27, 'Exercicios - Planejamento de Projetos Digitais', 'DOCX', '850 KB', 16);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (28, 'Apostila - SEO para Iniciantes', 'PDF', '2.0 MB', 17);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (29, 'Exercicios - SEO para Iniciantes', 'DOCX', '850 KB', 17);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (30, 'Apostila - Redes Sociais para Negocios', 'PDF', '2.0 MB', 18);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (31, 'Exercicios - Redes Sociais para Negocios', 'DOCX', '850 KB', 18);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (32, 'Apostila - Python para Data Science', 'PDF', '2.0 MB', 19);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (33, 'Exercicios - Python para Data Science', 'DOCX', '850 KB', 19);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (34, 'Apostila - Visualizacao de Dados', 'PDF', '2.0 MB', 20);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (35, 'Exercicios - Visualizacao de Dados', 'DOCX', '850 KB', 20);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (36, 'Apostila - Fundamentos de AWS', 'PDF', '2.0 MB', 21);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (37, 'Exercicios - Fundamentos de AWS', 'DOCX', '850 KB', 21);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (38, 'Apostila - Deploy de Aplicacoes na Nuvem', 'PDF', '2.0 MB', 22);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (39, 'Exercicios - Deploy de Aplicacoes na Nuvem', 'DOCX', '850 KB', 22);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (40, 'Apostila - Flutter para Iniciantes', 'PDF', '2.0 MB', 23);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (41, 'Exercicios - Flutter para Iniciantes', 'DOCX', '850 KB', 23);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (42, 'Apostila - UX para Aplicativos Mobile', 'PDF', '2.0 MB', 24);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (43, 'Exercicios - UX para Aplicativos Mobile', 'DOCX', '850 KB', 24);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (44, 'Apostila - Organizacao de Estudos', 'PDF', '2.0 MB', 25);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (45, 'Exercicios - Organizacao de Estudos', 'DOCX', '850 KB', 25);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (46, 'Apostila - Preparacao para Entrevistas Tech', 'PDF', '2.0 MB', 26);
INSERT INTO `tbl_materiais` (`id_material`, `nome_material`, `tipo_material`, `tam_arqu_material`, `fk_tbl_aulas_id_aula`) VALUES (47, 'Exercicios - Preparacao para Entrevistas Tech', 'DOCX', '850 KB', 26);

SET FOREIGN_KEY_CHECKS = 1;
