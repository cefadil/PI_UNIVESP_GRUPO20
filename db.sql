create table setores (id int not null auto_increment primary key , nome varchar(20), local varchar(20));
insert into setores (nome, local) values ('Recepção', 'Terreo');
insert into setores (nome, local) values ('Emergencia', 'Terreo');
insert into setores (nome, local) values ('Centro Cirurgico', '1 andar');

create table equipamentos (id int not null auto_increment primary key , descricao varchar(30), fabricante varchar(30), modelo varchar(30), num_serie varchar(30), tag varchar(30), local int, foreign key (local) references setores(id));
insert into equipamentos (descricao, fabricante, modelo, num_serie, tag, local) VALUES ('Espectrocromatografo Nuclear', 'Grupo 20 Corporation', 'NNM2024', 'ABXZ1245', 'TAG01', 1);
insert into equipamentos (descricao, fabricante, modelo, num_serie, tag, local) VALUES ('Montrologo Adverbial', 'NASA Creations', 'NSC24', 'ABXZ6969', 'TAG02', 3);
insert into equipamentos (descricao, fabricante, modelo, num_serie, tag, local) VALUES ('Ficticiometro', 'Creative Creators', 'CCCC4240', 'ZYX987', 'TAG02', 2);

create table usuarios( id int not null auto_increment primary key, nome varchar(50), senha varchar(50), matricula varchar(10), setor int, foreign key (setor) references setores(id));
insert into usuarios (nome, senha, matricula, setor) VALUES ('Eusebio', 'mamamia', '1234', 1);
insert into usuarios (nome, senha, matricula, setor) VALUES ('Godofredo', 'senhamuitoruim', '2345', 2);
insert into usuarios (nome, senha, matricula, setor) VALUES ('Almerinda', 'senha', '3456', 3);
insert into usuarios (nome, senha, matricula, setor) VALUES ('Veridiana', 'naoseicriarsenha', '4567', 3);


create table movimentacoes (id int not null auto_increment primary key, funcionario int not null, setor int not null, foreign key (funcionario) references usuarios(id), foreign key (setor) references setores(id));
insert into movimentacoes(funcionario, setor) VALUES (1, 2);
insert into movimentacoes(funcionario, setor) VALUES (3, 2);
insert into movimentacoes(funcionario, setor) VALUES (4, 1);
insert into movimentacoes(funcionario, setor) VALUES (1, 3);
