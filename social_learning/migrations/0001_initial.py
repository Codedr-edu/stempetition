# Generated by Django 4.2.6 on 2023-11-12 00:44

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
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('facebook', models.CharField(blank=True, max_length=1000, null=True)),
                ('instagram', models.CharField(blank=True, max_length=1000, null=True)),
                ('twitter', models.CharField(blank=True, max_length=1000, null=True)),
                ('zalo', models.CharField(blank=True, max_length=1000, null=True)),
                ('grade', models.IntegerField()),
                ('address', models.TextField()),
                ('address_password', models.TextField()),
                ('wallet_passcode', models.TextField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('thumnail', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('grade', models.IntegerField()),
                ('price', models.FloatField()),
                ('file', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('comment_counter', models.IntegerField()),
                ('dislike', models.ManyToManyField(blank=True, null=True, related_name='document_dislike', to='social_learning.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Education_rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gigs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('result', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('grade', models.IntegerField()),
                ('price', models.FloatField()),
                ('book_include', models.CharField(max_length=1000)),
                ('type_learn', models.CharField(max_length=1000)),
                ('comment_counter', models.IntegerField()),
                ('dislike', models.ManyToManyField(blank=True, null=True, related_name='gig_dislike', to='social_learning.bio')),
                ('education_rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Education_rank', to='social_learning.education_rank')),
                ('like', models.ManyToManyField(blank=True, null=True, related_name='gig_like', to='social_learning.bio')),
            ],
        ),
        migrations.CreateModel(
            name='join_cls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joined_gig', to='social_learning.gigs')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_join', to='social_learning.bio')),
            ],
        ),
        migrations.CreateModel(
            name='payment_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('schoolable', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_value', models.FloatField()),
                ('changed_value', models.FloatField()),
                ('done', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('change_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_currency', to='social_learning.payment_method')),
                ('changed_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency', to='social_learning.payment_method')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_method', to='social_learning.payment_method')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_user', to='social_learning.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('file', models.TextField(blank=True, null=True)),
                ('grade', models.IntegerField()),
                ('price', models.FloatField()),
                ('answered', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('comment_counter', models.IntegerField()),
                ('dislike', models.ManyToManyField(blank=True, null=True, related_name='question_dislike', to='social_learning.bio')),
                ('education_rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Education_rank_question', to='social_learning.education_rank')),
                ('like', models.ManyToManyField(blank=True, null=True, related_name='question_like', to='social_learning.bio')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='social_learning.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_user', to='social_learning.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('comment_counter', models.IntegerField()),
                ('dislike', models.ManyToManyField(blank=True, null=True, related_name='post_dislike_related', to='social_learning.bio')),
                ('like', models.ManyToManyField(blank=True, null=True, related_name='post_like_related', to='social_learning.bio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_auth_related', to='social_learning.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cls_day', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('check_stu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='check_stu', to='social_learning.join_cls')),
            ],
        ),
        migrations.CreateModel(
            name='have_buy_document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_check', to='social_learning.document')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Document_buyer', to='social_learning.bio')),
            ],
        ),
        migrations.AddField(
            model_name='gigs',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_choose', to='social_learning.subject'),
        ),
        migrations.AddField(
            model_name='gigs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gigs_auth', to='social_learning.bio'),
        ),
        migrations.AddField(
            model_name='document',
            name='edu_rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_edu_rank', to='social_learning.education_rank'),
        ),
        migrations.AddField(
            model_name='document',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='document_like', to='social_learning.bio'),
        ),
        migrations.AddField(
            model_name='document',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_subject', to='social_learning.subject'),
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Document_auth', to='social_learning.bio'),
        ),
        migrations.CreateModel(
            name='Comment_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('dislike', models.ManyToManyField(blank=True, null=True, related_name='comment_post_dislike_set', to='social_learning.bio')),
                ('like', models.ManyToManyField(blank=True, null=True, related_name='comment_post_like_set', to='social_learning.bio')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_post_related', to='social_learning.post')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_reply', to='social_learning.comment_post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_post_user_related', to='social_learning.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Gigs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_gigs', to='social_learning.gigs')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gigs_reply', to='social_learning.comment_gigs')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_gigs_user', to='social_learning.bio')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('dislike', models.ManyToManyField(blank=True, null=True, related_name='cmt_doc_dislike', to='social_learning.bio')),
                ('like', models.ManyToManyField(blank=True, null=True, related_name='cmt_doc_like', to='social_learning.bio')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cmt_document', to='social_learning.document')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_reply', to='social_learning.comment_document')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_document_user', to='social_learning.bio')),
            ],
        ),
        migrations.AddField(
            model_name='bio',
            name='edu_rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_edu_rank', to='social_learning.education_rank'),
        ),
        migrations.AddField(
            model_name='bio',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bio_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('file', models.TextField(blank=True, null=True)),
                ('choosen', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('dislike', models.ManyToManyField(blank=True, null=True, related_name='answer_dislike', to='social_learning.bio')),
                ('like', models.ManyToManyField(blank=True, null=True, related_name='answer_like', to='social_learning.bio')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ques_select', to='social_learning.question')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_reply', to='social_learning.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_user_answer', to='social_learning.bio')),
            ],
        ),
    ]