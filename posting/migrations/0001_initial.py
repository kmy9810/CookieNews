# Generated by Django 4.2 on 2023-04-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posting_category', models.CharField(choices=[('뉴스피드', '뉴스피드'), ('자유게시판', '자유게시판')], max_length=10)),
                ('posting_title', models.CharField(max_length=20)),
                ('posting_content', models.TextField()),
                ('posting_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Posting Created')),
            ],
            options={
                'db_table': 'my_board',
            },
        ),
    ]
