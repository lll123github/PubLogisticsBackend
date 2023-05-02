# Generated by Django 4.1.7 on 2023-05-02 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Line",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="线路列表编号"
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="线路名称")),
                (
                    "abbreviation",
                    models.CharField(blank=True, max_length=50, verbose_name="线路简称"),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="line_in_company",
                        to="company.company",
                        verbose_name="运营公司",
                    ),
                ),
            ],
        ),
    ]
