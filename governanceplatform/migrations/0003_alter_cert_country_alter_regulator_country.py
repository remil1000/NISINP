# Generated by Django 4.2 on 2024-07-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("governanceplatform", "0002_alter_company_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cert",
            name="country",
            field=models.CharField(
                choices=[
                    ("LU", "Luxembourg"),
                    ("BE", "Belgium"),
                    ("FR", "France"),
                    ("DE", "Germany"),
                    ("NL", "Netherlands"),
                    ("GB", "United Kingdom"),
                    ("AT", "Austria"),
                    ("BG", "Bulgaria"),
                    ("HR", "Croatia"),
                    ("CY", "Cyprus"),
                    ("CZ", "Czechia"),
                    ("DK", "Denmark"),
                    ("EE", "Estonia"),
                    ("FI", "Finland"),
                    ("GR", "Greece"),
                    ("HU", "Hungary"),
                    ("IE", "Ireland"),
                    ("IT", "Italy"),
                    ("LV", "Latvia"),
                    ("LT", "Lithuania"),
                    ("MT", "Malta"),
                    ("PL", "Poland"),
                    ("PT", "Portugal"),
                    ("RO", "Romania"),
                    ("SK", "Slovakia"),
                    ("SI", "Slovenia"),
                    ("ES", "Spain"),
                    ("SE", "Sweden"),
                    ("", "---------------------"),
                    ("AF", "Afghanistan"),
                    ("AX", "Åland Islands"),
                    ("AL", "Albania"),
                    ("DZ", "Algeria"),
                    ("AS", "American Samoa"),
                    ("AD", "Andorra"),
                    ("AO", "Angola"),
                    ("AI", "Anguilla"),
                    ("AQ", "Antarctica"),
                    ("AG", "Antigua and Barbuda"),
                    ("AR", "Argentina"),
                    ("AM", "Armenia"),
                    ("AW", "Aruba"),
                    ("AU", "Australia"),
                    ("AZ", "Azerbaijan"),
                    ("BS", "Bahamas"),
                    ("BH", "Bahrain"),
                    ("BD", "Bangladesh"),
                    ("BB", "Barbados"),
                    ("BY", "Belarus"),
                    ("BZ", "Belize"),
                    ("BJ", "Benin"),
                    ("BM", "Bermuda"),
                    ("BT", "Bhutan"),
                    ("BO", "Bolivia"),
                    ("BQ", "Bonaire, Sint Eustatius and Saba"),
                    ("BA", "Bosnia and Herzegovina"),
                    ("BW", "Botswana"),
                    ("BV", "Bouvet Island"),
                    ("BR", "Brazil"),
                    ("IO", "British Indian Ocean Territory"),
                    ("BN", "Brunei"),
                    ("BF", "Burkina Faso"),
                    ("BI", "Burundi"),
                    ("CV", "Cabo Verde"),
                    ("KH", "Cambodia"),
                    ("CM", "Cameroon"),
                    ("CA", "Canada"),
                    ("KY", "Cayman Islands"),
                    ("CF", "Central African Republic"),
                    ("TD", "Chad"),
                    ("CL", "Chile"),
                    ("CN", "China"),
                    ("CX", "Christmas Island"),
                    ("CC", "Cocos (Keeling) Islands"),
                    ("CO", "Colombia"),
                    ("KM", "Comoros"),
                    ("CG", "Congo"),
                    ("CD", "Congo (the Democratic Republic of the)"),
                    ("CK", "Cook Islands"),
                    ("CR", "Costa Rica"),
                    ("CI", "Côte d'Ivoire"),
                    ("CU", "Cuba"),
                    ("CW", "Curaçao"),
                    ("DJ", "Djibouti"),
                    ("DM", "Dominica"),
                    ("DO", "Dominican Republic"),
                    ("EC", "Ecuador"),
                    ("EG", "Egypt"),
                    ("SV", "El Salvador"),
                    ("GQ", "Equatorial Guinea"),
                    ("ER", "Eritrea"),
                    ("SZ", "Eswatini"),
                    ("ET", "Ethiopia"),
                    ("FK", "Falkland Islands (Malvinas)"),
                    ("FO", "Faroe Islands"),
                    ("FJ", "Fiji"),
                    ("GF", "French Guiana"),
                    ("PF", "French Polynesia"),
                    ("TF", "French Southern Territories"),
                    ("GA", "Gabon"),
                    ("GM", "Gambia"),
                    ("GE", "Georgia"),
                    ("GH", "Ghana"),
                    ("GI", "Gibraltar"),
                    ("GL", "Greenland"),
                    ("GD", "Grenada"),
                    ("GP", "Guadeloupe"),
                    ("GU", "Guam"),
                    ("GT", "Guatemala"),
                    ("GG", "Guernsey"),
                    ("GN", "Guinea"),
                    ("GW", "Guinea-Bissau"),
                    ("GY", "Guyana"),
                    ("HT", "Haiti"),
                    ("HM", "Heard Island and McDonald Islands"),
                    ("VA", "Holy See"),
                    ("HN", "Honduras"),
                    ("HK", "Hong Kong"),
                    ("IS", "Iceland"),
                    ("IN", "India"),
                    ("ID", "Indonesia"),
                    ("IR", "Iran"),
                    ("IQ", "Iraq"),
                    ("IM", "Isle of Man"),
                    ("IL", "Israel"),
                    ("JM", "Jamaica"),
                    ("JP", "Japan"),
                    ("JE", "Jersey"),
                    ("JO", "Jordan"),
                    ("KZ", "Kazakhstan"),
                    ("KE", "Kenya"),
                    ("KI", "Kiribati"),
                    ("KW", "Kuwait"),
                    ("KG", "Kyrgyzstan"),
                    ("LA", "Laos"),
                    ("LB", "Lebanon"),
                    ("LS", "Lesotho"),
                    ("LR", "Liberia"),
                    ("LY", "Libya"),
                    ("LI", "Liechtenstein"),
                    ("MO", "Macao"),
                    ("MG", "Madagascar"),
                    ("MW", "Malawi"),
                    ("MY", "Malaysia"),
                    ("MV", "Maldives"),
                    ("ML", "Mali"),
                    ("MH", "Marshall Islands"),
                    ("MQ", "Martinique"),
                    ("MR", "Mauritania"),
                    ("MU", "Mauritius"),
                    ("YT", "Mayotte"),
                    ("MX", "Mexico"),
                    ("FM", "Micronesia"),
                    ("MD", "Moldova"),
                    ("MC", "Monaco"),
                    ("MN", "Mongolia"),
                    ("ME", "Montenegro"),
                    ("MS", "Montserrat"),
                    ("MA", "Morocco"),
                    ("MZ", "Mozambique"),
                    ("MM", "Myanmar"),
                    ("NA", "Namibia"),
                    ("NR", "Nauru"),
                    ("NP", "Nepal"),
                    ("NC", "New Caledonia"),
                    ("NZ", "New Zealand"),
                    ("NI", "Nicaragua"),
                    ("NE", "Niger"),
                    ("NG", "Nigeria"),
                    ("NU", "Niue"),
                    ("NF", "Norfolk Island"),
                    ("KP", "North Korea"),
                    ("MK", "North Macedonia"),
                    ("MP", "Northern Mariana Islands"),
                    ("NO", "Norway"),
                    ("OM", "Oman"),
                    ("PK", "Pakistan"),
                    ("PW", "Palau"),
                    ("PS", "Palestine, State of"),
                    ("PA", "Panama"),
                    ("PG", "Papua New Guinea"),
                    ("PY", "Paraguay"),
                    ("PE", "Peru"),
                    ("PH", "Philippines"),
                    ("PN", "Pitcairn"),
                    ("PR", "Puerto Rico"),
                    ("QA", "Qatar"),
                    ("RE", "Réunion"),
                    ("RU", "Russia"),
                    ("RW", "Rwanda"),
                    ("BL", "Saint Barthélemy"),
                    ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
                    ("KN", "Saint Kitts and Nevis"),
                    ("LC", "Saint Lucia"),
                    ("MF", "Saint Martin (French part)"),
                    ("PM", "Saint Pierre and Miquelon"),
                    ("VC", "Saint Vincent and the Grenadines"),
                    ("WS", "Samoa"),
                    ("SM", "San Marino"),
                    ("ST", "Sao Tome and Principe"),
                    ("SA", "Saudi Arabia"),
                    ("SN", "Senegal"),
                    ("RS", "Serbia"),
                    ("SC", "Seychelles"),
                    ("SL", "Sierra Leone"),
                    ("SG", "Singapore"),
                    ("SX", "Sint Maarten (Dutch part)"),
                    ("SB", "Solomon Islands"),
                    ("SO", "Somalia"),
                    ("ZA", "South Africa"),
                    ("GS", "South Georgia and the South Sandwich Islands"),
                    ("KR", "South Korea"),
                    ("SS", "South Sudan"),
                    ("LK", "Sri Lanka"),
                    ("SD", "Sudan"),
                    ("SR", "Suriname"),
                    ("SJ", "Svalbard and Jan Mayen"),
                    ("CH", "Switzerland"),
                    ("SY", "Syria"),
                    ("TW", "Taiwan"),
                    ("TJ", "Tajikistan"),
                    ("TZ", "Tanzania"),
                    ("TH", "Thailand"),
                    ("TL", "Timor-Leste"),
                    ("TG", "Togo"),
                    ("TK", "Tokelau"),
                    ("TO", "Tonga"),
                    ("TT", "Trinidad and Tobago"),
                    ("TN", "Tunisia"),
                    ("TR", "Türkiye"),
                    ("TM", "Turkmenistan"),
                    ("TC", "Turks and Caicos Islands"),
                    ("TV", "Tuvalu"),
                    ("UG", "Uganda"),
                    ("UA", "Ukraine"),
                    ("AE", "United Arab Emirates"),
                    ("UM", "United States Minor Outlying Islands"),
                    ("US", "United States of America"),
                    ("UY", "Uruguay"),
                    ("UZ", "Uzbekistan"),
                    ("VU", "Vanuatu"),
                    ("VE", "Venezuela"),
                    ("VN", "Vietnam"),
                    ("VG", "Virgin Islands (British)"),
                    ("VI", "Virgin Islands (U.S.)"),
                    ("WF", "Wallis and Futuna"),
                    ("EH", "Western Sahara"),
                    ("YE", "Yemen"),
                    ("ZM", "Zambia"),
                    ("ZW", "Zimbabwe"),
                ],
                max_length=200,
                null=True,
                verbose_name="country",
            ),
        ),
        migrations.AlterField(
            model_name="regulator",
            name="country",
            field=models.CharField(
                choices=[
                    ("LU", "Luxembourg"),
                    ("BE", "Belgium"),
                    ("FR", "France"),
                    ("DE", "Germany"),
                    ("NL", "Netherlands"),
                    ("GB", "United Kingdom"),
                    ("AT", "Austria"),
                    ("BG", "Bulgaria"),
                    ("HR", "Croatia"),
                    ("CY", "Cyprus"),
                    ("CZ", "Czechia"),
                    ("DK", "Denmark"),
                    ("EE", "Estonia"),
                    ("FI", "Finland"),
                    ("GR", "Greece"),
                    ("HU", "Hungary"),
                    ("IE", "Ireland"),
                    ("IT", "Italy"),
                    ("LV", "Latvia"),
                    ("LT", "Lithuania"),
                    ("MT", "Malta"),
                    ("PL", "Poland"),
                    ("PT", "Portugal"),
                    ("RO", "Romania"),
                    ("SK", "Slovakia"),
                    ("SI", "Slovenia"),
                    ("ES", "Spain"),
                    ("SE", "Sweden"),
                    ("", "---------------------"),
                    ("AF", "Afghanistan"),
                    ("AX", "Åland Islands"),
                    ("AL", "Albania"),
                    ("DZ", "Algeria"),
                    ("AS", "American Samoa"),
                    ("AD", "Andorra"),
                    ("AO", "Angola"),
                    ("AI", "Anguilla"),
                    ("AQ", "Antarctica"),
                    ("AG", "Antigua and Barbuda"),
                    ("AR", "Argentina"),
                    ("AM", "Armenia"),
                    ("AW", "Aruba"),
                    ("AU", "Australia"),
                    ("AZ", "Azerbaijan"),
                    ("BS", "Bahamas"),
                    ("BH", "Bahrain"),
                    ("BD", "Bangladesh"),
                    ("BB", "Barbados"),
                    ("BY", "Belarus"),
                    ("BZ", "Belize"),
                    ("BJ", "Benin"),
                    ("BM", "Bermuda"),
                    ("BT", "Bhutan"),
                    ("BO", "Bolivia"),
                    ("BQ", "Bonaire, Sint Eustatius and Saba"),
                    ("BA", "Bosnia and Herzegovina"),
                    ("BW", "Botswana"),
                    ("BV", "Bouvet Island"),
                    ("BR", "Brazil"),
                    ("IO", "British Indian Ocean Territory"),
                    ("BN", "Brunei"),
                    ("BF", "Burkina Faso"),
                    ("BI", "Burundi"),
                    ("CV", "Cabo Verde"),
                    ("KH", "Cambodia"),
                    ("CM", "Cameroon"),
                    ("CA", "Canada"),
                    ("KY", "Cayman Islands"),
                    ("CF", "Central African Republic"),
                    ("TD", "Chad"),
                    ("CL", "Chile"),
                    ("CN", "China"),
                    ("CX", "Christmas Island"),
                    ("CC", "Cocos (Keeling) Islands"),
                    ("CO", "Colombia"),
                    ("KM", "Comoros"),
                    ("CG", "Congo"),
                    ("CD", "Congo (the Democratic Republic of the)"),
                    ("CK", "Cook Islands"),
                    ("CR", "Costa Rica"),
                    ("CI", "Côte d'Ivoire"),
                    ("CU", "Cuba"),
                    ("CW", "Curaçao"),
                    ("DJ", "Djibouti"),
                    ("DM", "Dominica"),
                    ("DO", "Dominican Republic"),
                    ("EC", "Ecuador"),
                    ("EG", "Egypt"),
                    ("SV", "El Salvador"),
                    ("GQ", "Equatorial Guinea"),
                    ("ER", "Eritrea"),
                    ("SZ", "Eswatini"),
                    ("ET", "Ethiopia"),
                    ("FK", "Falkland Islands (Malvinas)"),
                    ("FO", "Faroe Islands"),
                    ("FJ", "Fiji"),
                    ("GF", "French Guiana"),
                    ("PF", "French Polynesia"),
                    ("TF", "French Southern Territories"),
                    ("GA", "Gabon"),
                    ("GM", "Gambia"),
                    ("GE", "Georgia"),
                    ("GH", "Ghana"),
                    ("GI", "Gibraltar"),
                    ("GL", "Greenland"),
                    ("GD", "Grenada"),
                    ("GP", "Guadeloupe"),
                    ("GU", "Guam"),
                    ("GT", "Guatemala"),
                    ("GG", "Guernsey"),
                    ("GN", "Guinea"),
                    ("GW", "Guinea-Bissau"),
                    ("GY", "Guyana"),
                    ("HT", "Haiti"),
                    ("HM", "Heard Island and McDonald Islands"),
                    ("VA", "Holy See"),
                    ("HN", "Honduras"),
                    ("HK", "Hong Kong"),
                    ("IS", "Iceland"),
                    ("IN", "India"),
                    ("ID", "Indonesia"),
                    ("IR", "Iran"),
                    ("IQ", "Iraq"),
                    ("IM", "Isle of Man"),
                    ("IL", "Israel"),
                    ("JM", "Jamaica"),
                    ("JP", "Japan"),
                    ("JE", "Jersey"),
                    ("JO", "Jordan"),
                    ("KZ", "Kazakhstan"),
                    ("KE", "Kenya"),
                    ("KI", "Kiribati"),
                    ("KW", "Kuwait"),
                    ("KG", "Kyrgyzstan"),
                    ("LA", "Laos"),
                    ("LB", "Lebanon"),
                    ("LS", "Lesotho"),
                    ("LR", "Liberia"),
                    ("LY", "Libya"),
                    ("LI", "Liechtenstein"),
                    ("MO", "Macao"),
                    ("MG", "Madagascar"),
                    ("MW", "Malawi"),
                    ("MY", "Malaysia"),
                    ("MV", "Maldives"),
                    ("ML", "Mali"),
                    ("MH", "Marshall Islands"),
                    ("MQ", "Martinique"),
                    ("MR", "Mauritania"),
                    ("MU", "Mauritius"),
                    ("YT", "Mayotte"),
                    ("MX", "Mexico"),
                    ("FM", "Micronesia"),
                    ("MD", "Moldova"),
                    ("MC", "Monaco"),
                    ("MN", "Mongolia"),
                    ("ME", "Montenegro"),
                    ("MS", "Montserrat"),
                    ("MA", "Morocco"),
                    ("MZ", "Mozambique"),
                    ("MM", "Myanmar"),
                    ("NA", "Namibia"),
                    ("NR", "Nauru"),
                    ("NP", "Nepal"),
                    ("NC", "New Caledonia"),
                    ("NZ", "New Zealand"),
                    ("NI", "Nicaragua"),
                    ("NE", "Niger"),
                    ("NG", "Nigeria"),
                    ("NU", "Niue"),
                    ("NF", "Norfolk Island"),
                    ("KP", "North Korea"),
                    ("MK", "North Macedonia"),
                    ("MP", "Northern Mariana Islands"),
                    ("NO", "Norway"),
                    ("OM", "Oman"),
                    ("PK", "Pakistan"),
                    ("PW", "Palau"),
                    ("PS", "Palestine, State of"),
                    ("PA", "Panama"),
                    ("PG", "Papua New Guinea"),
                    ("PY", "Paraguay"),
                    ("PE", "Peru"),
                    ("PH", "Philippines"),
                    ("PN", "Pitcairn"),
                    ("PR", "Puerto Rico"),
                    ("QA", "Qatar"),
                    ("RE", "Réunion"),
                    ("RU", "Russia"),
                    ("RW", "Rwanda"),
                    ("BL", "Saint Barthélemy"),
                    ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
                    ("KN", "Saint Kitts and Nevis"),
                    ("LC", "Saint Lucia"),
                    ("MF", "Saint Martin (French part)"),
                    ("PM", "Saint Pierre and Miquelon"),
                    ("VC", "Saint Vincent and the Grenadines"),
                    ("WS", "Samoa"),
                    ("SM", "San Marino"),
                    ("ST", "Sao Tome and Principe"),
                    ("SA", "Saudi Arabia"),
                    ("SN", "Senegal"),
                    ("RS", "Serbia"),
                    ("SC", "Seychelles"),
                    ("SL", "Sierra Leone"),
                    ("SG", "Singapore"),
                    ("SX", "Sint Maarten (Dutch part)"),
                    ("SB", "Solomon Islands"),
                    ("SO", "Somalia"),
                    ("ZA", "South Africa"),
                    ("GS", "South Georgia and the South Sandwich Islands"),
                    ("KR", "South Korea"),
                    ("SS", "South Sudan"),
                    ("LK", "Sri Lanka"),
                    ("SD", "Sudan"),
                    ("SR", "Suriname"),
                    ("SJ", "Svalbard and Jan Mayen"),
                    ("CH", "Switzerland"),
                    ("SY", "Syria"),
                    ("TW", "Taiwan"),
                    ("TJ", "Tajikistan"),
                    ("TZ", "Tanzania"),
                    ("TH", "Thailand"),
                    ("TL", "Timor-Leste"),
                    ("TG", "Togo"),
                    ("TK", "Tokelau"),
                    ("TO", "Tonga"),
                    ("TT", "Trinidad and Tobago"),
                    ("TN", "Tunisia"),
                    ("TR", "Türkiye"),
                    ("TM", "Turkmenistan"),
                    ("TC", "Turks and Caicos Islands"),
                    ("TV", "Tuvalu"),
                    ("UG", "Uganda"),
                    ("UA", "Ukraine"),
                    ("AE", "United Arab Emirates"),
                    ("UM", "United States Minor Outlying Islands"),
                    ("US", "United States of America"),
                    ("UY", "Uruguay"),
                    ("UZ", "Uzbekistan"),
                    ("VU", "Vanuatu"),
                    ("VE", "Venezuela"),
                    ("VN", "Vietnam"),
                    ("VG", "Virgin Islands (British)"),
                    ("VI", "Virgin Islands (U.S.)"),
                    ("WF", "Wallis and Futuna"),
                    ("EH", "Western Sahara"),
                    ("YE", "Yemen"),
                    ("ZM", "Zambia"),
                    ("ZW", "Zimbabwe"),
                ],
                max_length=200,
                null=True,
                verbose_name="country",
            ),
        ),
    ]