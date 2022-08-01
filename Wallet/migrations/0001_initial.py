# Generated by Django 4.0.6 on 2022-08-01 16:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(default=0)),
                ('account_type', models.CharField(max_length=20, null=True)),
                ('balance', models.IntegerField()),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('country_of_origin', models.CharField(max_length=24, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('age', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=25, null=True)),
                ('phonenumber', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('nationality', models.CharField(max_length=20, null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=25, null=True)),
                ('receipt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('recipt_number', models.CharField(max_length=25, null=True)),
                ('total_Amount', models.IntegerField(default=0)),
                ('recipt_File', models.FileField(upload_to='wallet/')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipts_account', to='Wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=20, null=True)),
                ('pin', models.TextField(max_length=6, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_currency', to='Wallet.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wallet_customer', to='Wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_ref', models.CharField(max_length=255, null=True)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_type', models.CharField(choices=[('withdraw', 'Withdrawal'), ('depo', 'deposit')], max_length=10, null=True)),
                ('transaction_charge', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_destination_account', to='Wallet.account')),
                ('original_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_original_account', to='Wallet.account')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_receipt', to='Wallet.receipts')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='Wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('thirdparty_id', models.CharField(max_length=10, null=True)),
                ('phone_Number', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ThirdParty_account', to='Wallet.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ThirdParty_currency', to='Wallet.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('bonus', models.CharField(max_length=25, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_customer', to='Wallet.customer')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reward_transaction', to='Wallet.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='receipts',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipts_transaction', to='Wallet.transaction'),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_Id', models.CharField(max_length=25, null=True)),
                ('status', models.CharField(choices=[('read', 'read'), ('unread', 'unread')], max_length=12, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notifications_recipient', to='Wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField()),
                ('loan_type', models.CharField(max_length=25, null=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('interest_rate', models.IntegerField()),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('loan_balance', models.IntegerField()),
                ('loan_term', models.IntegerField()),
                ('guaranter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_guaranter', to='Wallet.customer')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Loan_wallet', to='Wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Issued', models.DateTimeField(default=django.utils.timezone.now)),
                ('card_name', models.CharField(max_length=20, null=True)),
                ('card_number', models.IntegerField()),
                ('card_type', models.CharField(choices=[('Master', 'Mastercard'), ('visa', 'visacard')], max_length=10, null=True)),
                ('expiry_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('card_status', models.CharField(choices=[('d', 'debit'), ('c', 'credit')], max_length=1, null=True)),
                ('cvv_security', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_account', to='Wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Card_wallet', to='Wallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Account_wallet', to='Wallet.wallet'),
        ),
    ]
