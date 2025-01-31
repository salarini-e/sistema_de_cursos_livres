# Generated by Django 3.2.15 on 2022-08-24 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=150, verbose_name='CPF')),
                ('dt_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Qual foi o sexo atribuído no seu nascimento?')),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=12)),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome da categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('carga_horaria', models.CharField(max_length=150)),
                ('descricao', models.TextField(default='')),
                ('ativo', models.BooleanField(default=True)),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
                ('dt_alteracao', models.DateField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do local')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(max_length=150)),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
                ('dt_alteracao', models.DateField(auto_now=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
                ('user_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TurmaUserInclusao', to=settings.AUTH_USER_MODEL)),
                ('user_ultima_alteracao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TurmaUserAlteracao', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Selecionado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_matricula', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.turma')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.instituicao'),
        ),
        migrations.AddField(
            model_name='curso',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.local'),
        ),
        migrations.AddField(
            model_name='curso',
            name='user_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userInclusao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='user_ultima_alteracao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userAlteracao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='candidato',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='selecionado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.selecionado'),
        ),
    ]
