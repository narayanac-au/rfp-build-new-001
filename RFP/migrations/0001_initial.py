# Generated by Django 4.1.7 on 2023-02-26 10:59

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Approval",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("rfp_id", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("industry", models.CharField(max_length=50)),
                ("Section", models.TextField(blank=True, null=True)),
                ("Sub_Section", models.TextField(blank=True, null=True)),
                ("Questions", models.TextField(blank=True, null=True)),
                ("options1", models.TextField(blank=True, null=True)),
                ("options2", models.TextField(blank=True, null=True)),
                ("options3", models.TextField(blank=True, null=True)),
                (
                    "approved",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="Approved"
                    ),
                ),
                ("answer", models.TextField(blank=True, null=True)),
                ("Model_Image_Link_BLOB", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="askques",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.CharField(
                        blank=True, max_length=200, null=True, unique=True
                    ),
                ),
                ("selected", models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DropQuery",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("user", models.CharField(blank=True, max_length=200, null=True)),
                ("question", models.TextField(blank=True, null=True)),
                ("answer1", models.TextField(blank=True, null=True)),
                ("answer2", models.TextField(blank=True, null=True)),
                ("answer3", models.TextField(blank=True, null=True)),
                ("select1", models.CharField(blank=True, max_length=10, null=True)),
                ("select2", models.CharField(blank=True, max_length=10, null=True)),
                ("select3", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "optionselect",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="First_Page",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("industry", models.CharField(max_length=50)),
                ("pic1", models.ImageField(upload_to="First_page_upload/Manual")),
                ("pic2", models.ImageField(upload_to="First_page_upload/Manual")),
                ("pic3", models.ImageField(upload_to="First_page_upload/Manual")),
                ("options1", models.CharField(blank=True, max_length=10, null=True)),
                ("options2", models.CharField(blank=True, max_length=10, null=True)),
                ("options3", models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="First_Page_upload",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("user", models.CharField(blank=True, max_length=200, null=True)),
                ("clientgeo", models.CharField(blank=True, max_length=200, null=True)),
                ("picdown", models.ImageField(upload_to="First_page_upload/Drop")),
            ],
        ),
        migrations.CreateModel(
            name="info",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "clientfullname",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "clientshortname",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "clientindustry",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("clientgeo", models.CharField(blank=True, max_length=200, null=True)),
                ("KPMGgeo", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "clientaddress_line1",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "clientaddress_line2",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "clientPostal_Code",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "KPMGaddress1",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KPMGgeo",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("KPMGgeo", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("user", models.CharField(blank=True, max_length=200, null=True)),
                ("clientgeo", models.CharField(blank=True, max_length=200, null=True)),
                ("picup", models.ImageField(upload_to="pickupdir/")),
            ],
        ),
        migrations.CreateModel(
            name="project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("content", django_quill.fields.QuillField(default="Hello")),
            ],
        ),
        migrations.CreateModel(
            name="SelectDropQuery",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("user", models.CharField(blank=True, max_length=200, null=True)),
                ("question", models.TextField(blank=True, null=True)),
                ("answer1", models.TextField(blank=True, null=True)),
                ("answer2", models.TextField(blank=True, null=True)),
                ("answer3", models.TextField(blank=True, null=True)),
                ("select1", models.CharField(blank=True, max_length=10, null=True)),
                ("select2", models.CharField(blank=True, max_length=10, null=True)),
                ("select3", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "optionselect",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserQuery",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("user", models.CharField(blank=True, max_length=200, null=True)),
                ("rfp_id", models.CharField(blank=True, max_length=50, null=True)),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                ("industry", models.CharField(blank=True, max_length=50, null=True)),
                ("Section", models.TextField(blank=True, null=True)),
                ("Sub_Section", models.TextField(blank=True, null=True)),
                ("query", models.TextField(blank=True, null=True)),
                ("answer1", models.TextField(blank=True, null=True)),
                ("answer2", models.TextField(blank=True, null=True)),
                ("answer3", models.TextField(blank=True, null=True)),
                (
                    "sentapproval",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("approved", models.CharField(blank=True, max_length=50, null=True)),
                ("viewed", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserQuestion",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("rfp_id", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "content_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("industry", models.CharField(blank=True, max_length=50, null=True)),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                ("Section", models.TextField(blank=True, null=True)),
                ("Sub_Section", models.TextField(blank=True, null=True)),
                ("question", models.TextField(blank=True, null=True)),
                ("Document_link", models.FileField(null=True, upload_to="")),
                (
                    "Approved",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="Approved"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=200)),
            ],
            options={"ordering": ["user"],},
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("rfp_id", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=50)),
                ("industry", models.CharField(max_length=50)),
                ("Section", models.TextField(blank=True, null=True)),
                ("Sub_Section", models.TextField(blank=True, null=True)),
                ("Questions", models.TextField(blank=True, null=True)),
                ("options1", models.TextField(blank=True, null=True)),
                ("options2", models.TextField(blank=True, null=True)),
                ("options3", models.TextField(blank=True, null=True)),
                ("Tick1", models.CharField(blank=True, max_length=10, null=True)),
                ("answer", models.TextField(blank=True, null=True)),
                ("Model_Image_Link_BLOB", models.URLField(blank=True, null=True)),
                ("Binaryword", models.BinaryField(blank=True, null=True)),
                ("Binarypic", models.BinaryField(blank=True, null=True)),
                ("File", models.FileField(blank=True, null=True, upload_to="files")),
                ("user", models.ManyToManyField(blank=True, null=True, to="RFP.users")),
            ],
        ),
        migrations.CreateModel(
            name="KPMGadd",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("originaladdress", models.CharField(max_length=200)),
                (
                    "KPMGgeo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="RFP.kpmggeo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("caption", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="./media/"),
                ),
                ("selected", models.CharField(blank=True, max_length=10, null=True)),
                ("user", models.ManyToManyField(blank=True, null=True, to="RFP.users")),
            ],
        ),
        migrations.CreateModel(
            name="Document_usercopy",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("country", models.CharField(max_length=50)),
                ("File", models.FileField(blank=True, null=True, upload_to="files")),
                ("user", models.ManyToManyField(blank=True, to="RFP.users")),
            ],
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                ("id", models.IntegerField(primary_key="TRUE", serialize=False)),
                ("country", models.CharField(max_length=50)),
                ("industry", models.CharField(max_length=50)),
                ("doc_index", models.CharField(blank=True, max_length=100, null=True)),
                ("selected", models.CharField(blank=True, max_length=10, null=True)),
                ("File", models.FileField(blank=True, null=True, upload_to="files")),
                ("user", models.ManyToManyField(blank=True, to="RFP.users")),
            ],
            options={"ordering": ["country"],},
        ),
    ]
