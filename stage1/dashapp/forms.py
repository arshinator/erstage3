from django import forms


class UploadForms(forms.Form):
    YEAR = (
        ('None', 'None'),
        ('Financial Year 2015-16', 'Financial Year 2015-16'),
        ('Financial Year 2014-15', 'Financial Year 2014-15'),
        ('Financial Year 2013-14', 'Financial Year 2013-14'),
        ('Financial Year 2012-13', 'Financial Year 2012-13'),
        ('Financial Year 2011-12', 'Financial Year 2011-12'),

    )

    NSC = (
        ('None', 'None'),
        ('Financial Year 2015-16', 'Financial Year 2015-16'),
        ('Financial Year 2014-15', 'Financial Year 2014-15'),
        ('Financial Year 2013-14', 'Financial Year 2013-14'),
        ('Financial Year 2012-13', 'Financial Year 2012-13'),
        ('Financial Year 2011-12', 'Financial Year 2011-12'),

    )

    DONATIONS = (
        ('None', 'None'),
        ('National Defence Fund set up by the Central Government',
         'National Defence Fund set up by the Central Government'),

        ('Prime Minister\'s National Relief Fund', 'Prime Minister\'s National Relief Fund'),
        ('National Foundation for Communal Harmony', 'National Foundation for Communal Harmony'),
        ('Zila Saksharta Samiti ', 'Zila Saksharta Samiti '),
        ('National Illness Assistance Fund', 'National Illness Assistance Fund'),
        ('National Blood Transfusion Council ', 'National Blood Transfusion Council '),
        (
            'National Trust for Welfare of Persons with Autism, Cerebral Palsy, Mental Retardation and Multiple Disabilities',
            'National Trust for Welfare of Persons with Autism, Cerebral Palsy, Mental Retardation and Multiple Disabilities'),

        ('National Sports Fund', 'National Sports Fund'),
        ('National Cultural Fund', 'National Cultural Fund'),

        ('Fund for Technology Development and Application', 'Fund for Technology Development and Application'),
        ('National Children\'s Fund', 'National Children\'s Fund'),
        ('Chief Minister\'s Relief Fund ', 'Chief Minister\'s Relief Fund '),
        ('The Army Central Welfare Fund or the Indian Naval ', 'The Army Central Welfare Fund or the Indian Naval '),
        ('Prime Minister\'s Armenia Earthquake Relief Fund', 'Prime Minister\'s Armenia Earthquake Relief Fund'),
        ('Africa (Public Contributions - India) Fund', 'Africa (Public Contributions - India) Fund'),
        ('Swachh Bharat Kosh (applicable from FY 2014-15)', 'Swachh Bharat Kosh (applicable from FY 2014-15)'),
        ('Clean Ganga Fund (applicable from FY 2014-15)', 'Clean Ganga Fund (applicable from FY 2014-15)'),
        ('National Fund for Control of Drug Abuse (applicable from FY 2015-16)',
         'National Fund for Control of Drug Abuse (applicable from FY 2015-16)'),
        ('Jawaharlal Nehru Memorial Fund', 'Jawaharlal Nehru Memorial Fund'),
        ('Prime Minister\'s Drought Relief Fund', 'Prime Minister\'s Drought Relief Fund'),
        ('Indira Gandhi Memorial Trust', 'Indira Gandhi Memorial Trust'),
        ('Rajiv Gandhi Foundation', 'Rajiv Gandhi Foundation'),

    )

    TIME = (
        ('8 am - 9 am', '8 am - 9 am'),
        ('9 am - 10 am', '9 am - 10 am'),
        ('10 am - 11 am', '10 am - 11 am'),
        ('11 am - 12 pm', '11 am - 12 pm'),
        ('12 pm - 1 pm', '12 pm - 1 pm'),
        ('1 pm - 2 pm', '1 pm - 2 pm'),
        ('2 pm - 3 pm', '2 pm - 3 pm'),
        ('3 pm - 4 pm', '3 pm - 4 pm'),
        ('4 pm - 5 pm', '4 pm - 5 pm'),
        ('5 pm - 6 pm', '5 pm - 6 pm'),
        ('7 pm - 8 pm', '7 pm - 8 pm'),
        ('8 pm - 9 pm', '8 pm - 9 pm'),
        ('9 pm - 10 pm', '9 pm - 10 pm'),

    )

    yr = forms.ChoiceField(choices=YEAR)

    # detail = forms.CharField(max_length=100)
    first_interest = forms.CharField(max_length=100)
    first_principal = forms.CharField(max_length=100)

    other_rent = forms.CharField(max_length=100)
    other_tax = forms.CharField(max_length=100)
    other_interest = forms.CharField(max_length=100)
    other_principal = forms.CharField(max_length=100)

    interest_due = forms.CharField(max_length=100)
    p_repayment = forms.CharField(max_length=100)

    save_acc = forms.CharField(max_length=100)
    fixed_deposit = forms.CharField(max_length=100)
    kvp_ivp = forms.CharField(max_length=100)
    nsc_1 = forms.CharField(max_length=100)
    nsc_2 = forms.CharField(max_length=100)
    nsc_3 = forms.CharField(max_length=100)
    b_d = forms.CharField(max_length=100)
    i_property = forms.CharField(max_length=100)
    ppf = forms.CharField(max_length=100)
    pension = forms.CharField(max_length=100)
    lic = forms.CharField(max_length=100)
    fdr = forms.CharField(max_length=100)
    fees = forms.CharField(max_length=100)
    mf_uti = forms.CharField(max_length=100)
    n_pension = forms.CharField(max_length=100)
    edu_loan = forms.CharField(max_length=100)

    m_parent = forms.CharField(max_length=100)
    m_you = forms.CharField(max_length=100)

    d11 = forms.CharField(max_length=100)
    d12 = forms.CharField(max_length=100)
    d21 = forms.CharField(max_length=100)
    d22 = forms.CharField(max_length=100)
    d31 = forms.CharField(max_length=100)
    d32 = forms.CharField(max_length=100)

    section_1 = forms.CharField(max_length=100)
    section_2 = forms.CharField(max_length=100)

    other_deduct = forms.CharField(widget=forms.Textarea)

    fd_1 = forms.ChoiceField(choices=NSC)
    fd_2 = forms.ChoiceField(choices=NSC)
    fd_3 = forms.ChoiceField(choices=NSC)

    d_1 = forms.ChoiceField(choices=DONATIONS)
    d_2 = forms.ChoiceField(choices=DONATIONS)
    d_3 = forms.ChoiceField(choices=DONATIONS)

    acc = forms.CharField(max_length=100)
    ifsc = forms.CharField(max_length=100)

    time = forms.ChoiceField(choices=TIME)
