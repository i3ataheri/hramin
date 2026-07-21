import json, os

translations = {
    'ar': {
        'title': 'المتجر',
        'about_title': 'عن المنتج',
        'about_text': 'منتجاتنا تجمع بين الجمال والتقنية. كل منتج مزود بشريحة NFC تفتح لك عالم الحرمين الشريفين عند لمسها بهاتفك. تصميم أنيق ومتين يجعلها هدية مثالية لمحبي الأماكن المقدسة.',
        'products_title': 'المنتجات',
        'product_keychain': 'سلسلة مفاتيح NFC',
        'product_keychain_desc': 'تصميم أنيق بأشكال إسلامية، مزودة بشريحة NFC فتح تلقائياً عند قربها من الهاتف',
        'product_card': 'بطاقة NFC',
        'product_card_desc': 'بطاقة صغيرة الحجم سهلة الحمل، تحتوي على شريحة NFC لفتح التطبيق مباشرة',
        'product_phone': 'غطاء هاتف NFC',
        'product_phone_desc': 'غطاء هاتف متوافق مع مختلف الأجهزة، يحتوي على شريحة NFC مدمجة',
        'contact_title': 'التواصل مع البائعين',
        'how_title': 'كيف تحصل على المنتج',
        'contacts': [
            {'label': 'واتساب', 'value': '+966500000000'},
            {'label': 'بريد إلكتروني', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'اختر المنتج المناسب من المتاجر المعتمدة',
            'تواصل مع البائع عبر واتساب أو البريد الإلكتروني',
            'اختر طريقة الدفع والشحن المناسبة',
            'استلم المنتج واستمتع بتجربة فريدة'
        ]
    },
    'fa': {
        'title': 'فروشگاه',
        'about_title': 'درباره محصول',
        'about_text': 'محصولات ما زیبایی و فناوری را ترکیب می‌کنند. هر محصول مجهز به تراشه NFC است که با لمس گوشی، دنیای حرمین شریفین را برای شما باز می‌کند. طراحی شیک و بادوام، هدیه‌ای ایده‌آل برای علاقه‌مندان به اماکن مقدس.',
        'products_title': 'محصولات',
        'product_keychain': 'جاکلیدی NFC',
        'product_keychain_desc': 'طراحی شیک با اشکال اسلامی، مجهز به تراشه NFC که با نزدیک کردن به گوشی باز می‌شود',
        'product_card': 'کارت NFC',
        'product_card_desc': 'کارت کوچک و سبک، حاوی تراشه NFC برای باز کردن مستقیم برنامه',
        'product_phone': 'کاور گوشی NFC',
        'product_phone_desc': 'کاور گوشی سازگار با دستگاه‌های مختلف، با تراشه NFC تعبیه شده',
        'contact_title': 'ارتباط با فروشندگان',
        'how_title': 'نحوه دریافت محصول',
        'contacts': [
            {'label': 'واتساپ', 'value': '+966500000000'},
            {'label': 'ایمیل', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'محصول مناسب را از فروشگاه‌های معتبر انتخاب کنید',
            'از طریق واتساپ یا ایمیل با فروشنده تماس بگیرید',
            'روش پرداخت و ارسال مناسب را انتخاب کنید',
            'محصول را دریافت و از تجربه منحصربفرد لذت ببرید'
        ]
    },
    'en': {
        'title': 'Shop',
        'about_title': 'About Products',
        'about_text': 'Our products combine beauty with technology. Each product features an NFC chip that opens the world of the Holy Sites when you tap your phone. Elegant and durable design makes them a perfect gift for lovers of sacred places.',
        'products_title': 'Products',
        'product_keychain': 'NFC Keychain',
        'product_keychain_desc': 'Elegant design with Islamic patterns, equipped with NFC chip that activates when near your phone',
        'product_card': 'NFC Card',
        'product_card_desc': 'Compact and lightweight card with NFC chip for direct app access',
        'product_phone': 'NFC Phone Case',
        'product_phone_desc': 'Compatible phone case with built-in NFC chip for seamless experience',
        'contact_title': 'Contact Sellers',
        'how_title': 'How to Get the Product',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Choose the right product from authorized stores',
            'Contact the seller via WhatsApp or email',
            'Choose your preferred payment and shipping method',
            'Receive your product and enjoy a unique experience'
        ]
    },
    'ur': {
        'title': 'دکان',
        'about_title': 'مہمل کے بارے میں',
        'about_text': 'ہمارے مہمل خوبصورتی اور ٹیکنالوجی کو ملاتے ہیں۔ ہر مہمل میں NFC چپ ہے جو آپ کے فون کو چھونے پر حرمتین شریفین کی دنیا کھولتا ہے۔',
        'products_title': 'مہمل',
        'product_keychain': 'NFC چابی کا زنجیر',
        'product_keychain_desc': 'اسلامی نقوش کے ساتھ خوبصورت ڈیزائن، NFC چپ سے لیس',
        'product_card': 'NFC کارڈ',
        'product_card_desc': 'compact NFC کارڈ براہ راست ایپ تک رسائی کے لیے',
        'product_phone': 'NFC فون کا کور',
        'product_phone_desc': 'مختلف آلات کے ساتھ مطابقت پذیر، مضمون NFC چپ',
        'contact_title': 'بیچنے والوں سے رابطہ',
        'how_title': 'مہمل کیسے حاصل کریں',
        'contacts': [
            {'label': 'واٹس ایپ', 'value': '+966500000000'},
            {'label': 'ای میل', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'مستند دکانوں سے مناسب مہمل منتخب کریں',
            'واٹس ایپ یا ای میل کے ذریعے بیچنے والے سے رابطہ کریں',
            'ادائیگی اور شپنگ کا طریقہ منتخب کریں',
            'مہمل حاصل کریں اور منفرد تجربے سے لطف اندوز ہوں'
        ]
    },
    'id': {
        'title': 'Toko',
        'about_title': 'Tentang Produk',
        'about_text': 'Produk kami menggabungkan keindahan dengan teknologi. Setiap produk dilengkapi chip NFC yang membuka dunia Tanah Suci saat Anda menyentuhkannya ke ponsel.',
        'products_title': 'Produk',
        'product_keychain': 'Gantungan Kunci NFC',
        'product_keychain_desc': 'Desain elegan dengan pola Islam, dilengkapi chip NFC',
        'product_card': 'Kartu NFC',
        'product_card_desc': 'Kartu kompak dengan chip NFC untuk akses langsung',
        'product_phone': 'Case HP NFC',
        'product_phone_desc': 'Case kompatibel dengan chip NFC terintegrasi',
        'contact_title': 'Hubungi Penjual',
        'how_title': 'Cara Mendapatkan Produk',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Pilih produk yang sesuai dari toko resmi',
            'Hubungi penjual melalui WhatsApp atau email',
            'Pilih metode pembayaran dan pengiriman',
            'Terima produk dan nikmati pengalaman unik'
        ]
    },
    'bn': {
        'title': 'দোকান',
        'about_title': 'পণ্য সম্পর্কে',
        'about_text': 'আমাদের পণ্য সৌন্দর্য এবং প্রযুক্তিকে একত্রিত করে। প্রতিটি পণ্যে NFC চিপ রয়েছে যা আপনার ফোনে স্পর্শ করলে পবিত্র স্থানের জগৎ উন্মোচন করে।',
        'products_title': 'পণ্য',
        'product_keychain': 'NFC চাবির রিং',
        'product_keychain_desc': 'ইসলামিক নকশা সহ সুন্দর ডিজাইন, NFC চিপ সহ',
        'product_card': 'NFC কার্ড',
        'product_card_desc': 'সরাসরি অ্যাপ অ্যাক্সেসের জন্য কম্প্যাক্ট NFC কার্ড',
        'product_phone': 'NFC ফোন কেস',
        'product_phone_desc': 'বিভিন্ন ডিভাইসের সাথে সামঞ্জস্যপূর্ণ, ইনবিল্ট NFC চিপ',
        'contact_title': 'বিক্রেতাদের সাথে যোগাযোগ',
        'how_title': 'পণ্য কিভাবে পাবেন',
        'contacts': [
            {'label': 'হোয়াটসঅ্যাপ', 'value': '+966500000000'},
            {'label': 'ইমেইল', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'অনুমোদিত দোকান থেকে উপযুক্ত পণ্য বাছাই করুন',
            'হোয়াটসঅ্যাপ বা ইমেইলের মাধ্যমে বিক্রেতার সাথে যোগাযোগ করুন',
            'পেমেন্ট এবং শিপিং পদ্ধতি বাছাই করুন',
            'পণ্য গ্রহণ করুন এবং অনন্য অভিজ্ঞতা উপভোগ করুন'
        ]
    },
    'tr': {
        'title': 'Ma\u011faza',
        'about_title': 'U\u00fcr\u00fcnler Hakk\u0131nda',
        'about_text': 'U\u00fcr\u00fcnlerimiz g\u00fczelli\u011fi teknolojiyle bulu\u015fturur. Her \u00fcr\u00fcnde NFC \u00e7ipi bulunur, telefonunuzla dokundu\u011funuzda kutsal mekanlar\u0131n d\u00fcnyas\u0131n\u0131 a\u00e7ar.',
        'products_title': 'U\u00fcr\u00fcnler',
        'product_keychain': 'NFC Anahtarl\u0131k',
        'product_keychain_desc': 'Islami desenlerle zarif tasar\u0131m, NFC \u00e7ipli',
        'product_card': 'NFC Kart',
        'product_card_desc': 'Do\u011frudan uygulama eri\u015fimi i\u00e7in kompakt NFC kart',
        'product_phone': 'NFC K\u0131l\u0131f',
        'product_phone_desc': 'Dahili NFC \u00e7ipli uyumlu telefon k\u0131l\u0131f\u0131',
        'contact_title': 'Sat\u0131c\u0131larla \u0130leti\u015fim',
        'how_title': '\u00dcr\u00fcn\u00fc Nas\u0131l Alabilirsiniz',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'E-posta', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Yetkili ma\u011fazalardan do\u011fru \u00fcr\u00fcn\u00fc se\u00e7in',
            'WhatsApp veya e-posta ile sat\u0131c\u0131yla ileti\u015fime ge\u00e7in',
            '\u00d6deme ve g\u00f6nderim y\u00f6ntemini se\u00e7in',
            '\u00dcr\u00fcn\u00fcn\u00fcz\u00fc al\u0131n ve benzersiz bir deneyim ya\u015fay\u0131n'
        ]
    },
    'ms': {
        'title': 'Kedai',
        'about_title': 'Tentang Produk',
        'about_text': 'Produk kami menggabungkan keindahan dengan teknologi. Setiap produk dilengkapi cip NFC yang membuka dunia Tanah Suci apabila anda menyentuhkannya ke telefon.',
        'products_title': 'Produk',
        'product_keychain': 'Gigi Kunci NFC',
        'product_keychain_desc': 'Reka bentuk elegan dengan corak Islam, dilengkapi cip NFC',
        'product_card': 'Kad NFC',
        'product_card_desc': 'Kad kompak dengan cip NFC untuk akses terus',
        'product_phone': 'Sarung Telefon NFC',
        'product_phone_desc': 'Sarung serasi dengan cip NFC terbina dalam',
        'contact_title': 'Hubungi Penjual',
        'how_title': 'Cara Mendapatkan Produk',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Emel', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Pilih produk yang sesuai dari kedai rasmi',
            'Hubungi penjual melalui WhatsApp atau emel',
            'Pilih kaedah pembayaran dan penghantaran',
            'Terima produk dan nikmati pengalaman unik'
        ]
    },
    'fr': {
        'title': 'Boutique',
        'about_title': '\u00c0 Propos des Produits',
        'about_text': 'Nos produits allient beaut\u00e9 et technologie. Chaque produit dispose d\'une puce NFC qui ouvre le monde des Lieux Saints lorsque vous touchez votre t\u00e9l\u00e9phone.',
        'products_title': 'Produits',
        'product_keychain': 'Porte-cl\u00e9s NFC',
        'product_keychain_desc': 'Design \u00e9l\u00e9gant avec motifs islamiques, \u00e9quip\u00e9 d\'une puce NFC',
        'product_card': 'Carte NFC',
        'product_card_desc': 'Carte compacte avec puce NFC pour un acc\u00e8s direct',
        'product_phone': '\u00c9tui T\u00e9l\u00e9phone NFC',
        'product_phone_desc': '\u00c9tui compatible avec puce NFC int\u00e9gr\u00e9e',
        'contact_title': 'Contacter les Vendeurs',
        'how_title': 'Comment Obtenir le Produit',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Choisissez le produit dans les boutiques agr\u00e9\u00e9es',
            'Contactez le vendeur via WhatsApp ou email',
            'Choisissez votre mode de paiement et livraison',
            'Recevez votre produit et profitez d\'une exp\u00e9rience unique'
        ]
    },
    'sw': {
        'title': 'Duka',
        'about_title': 'Kuhusu Bidhaa',
        'about_text': 'Bidhaa zetu zinaunganisha uzuri na teknolojia. Kila bidhaa ina NFC chip inayofungua ulimwengu wa Maeneo Takatifu unapolinga simu yako.',
        'products_title': 'Bidhaa',
        'product_keychain': 'Mfunguo NFC',
        'product_keychain_desc': 'Muundo wa kifahari na michoro ya Kiislamu, yenye NFC chip',
        'product_card': 'Kadi ya NFC',
        'product_card_desc': 'Kadi ndogo yenye NFC chip kwa upatikanaji wa moja kwa moja',
        'product_phone': 'Gesi ya Simu NFC',
        'product_phone_desc': 'Gesi inayofanana yenye NFC chip iliyojengwa ndani',
        'contact_title': 'Wasiliana na Wauzaji',
        'how_title': 'Jinsi ya Kupata Bidhaa',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Barua Pepe', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Chagua bidhaa inayofaa kutoka duka rasmi',
            'Wasiliana na muuzaji kupitia WhatsApp au barua pepe',
            'Chagua njia ya malipo na usafirishaji',
            'Pokea bidhaa yako na furahia uzoefu wa kipekee'
        ]
    },
    'ha': {
        'title': 'Shago',
        'about_title': 'Game da Kayayyaki',
        'about_text': 'Kayayyakmu haɗa kyau da fasaha. Kowace kayayyaki tana da NFC chip da ke buɗe duniyar wurare masu tsarki lokacin da ka taɓa wayar ka.',
        'products_title': 'Kayayyaki',
        'product_keychain': 'Maballin NFC',
        'product_keychain_desc': 'Tsarin kyau tare da salon Islama, tare da NFC chip',
        'product_card': 'Katin NFC',
        'product_card_desc': 'Katin ƙarami tare da NFC chip don samun dama kai tsaye',
        'product_phone': 'Rufin Wayar NFC',
        'product_phone_desc': 'Rufin da ya dace tare da NFC chip a ciki',
        'contact_title': 'Tuntuɓi Masu Sayarwa',
        'how_title': 'Yadda za a Sami Kayayyaki',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Imel', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Zaɓi kayayyakin da ya dace daga shago masu amincewa',
            'Tuntuɓi mai sayarwa ta hanyar WhatsApp ko imel',
            'Zaɓi hanyar biya da kayan aiki',
            'Sami kayayyaki kuma ji daɗin ƙwarewa ta musamman'
        ]
    },
    'ps': {
        'title': 'پلورنه',
        'about_title': 'د محصول په اړه',
        'about_text': 'زموږ محصولات ښکلا او ټکنالوژي غواړي. هر محصول د NFC چپ سره مجهز دی چې تاسو د تلیفون لمس کولو سره د مقدس پلاو دنیا خلاصوي.',
        'products_title': 'محصولات',
        'product_keychain': 'NFC کیلي زنجیر',
        'product_keychain_desc': 'اسلامي نقوښو سره ښکلدار ډیزاین، د NFC چپ سره',
        'product_card': 'NFC کارت',
        'product_card_desc': 'د براہ راست ایپ ته رسیدو لپاره ټیټ NFC کارت',
        'product_phone': 'NFC تلیفون کیس',
        'product_phone_desc': 'د جوړ شوې NFC چپ سره مطابق کیس',
        'contact_title': 'د پلرونو سره اړیکه',
        'how_title': 'څنګه محصول تر لاسه ورکړئ',
        'contacts': [
            {'label': 'واتساپ', 'value': '+966500000000'},
            {'label': 'ایمیل', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'د تصدیق شوو پلورنو څخه مناسب محصول غوره کړئ',
            'واتساپ یا ایمیل له لارې د پلرونو سره اړیکه ونیسئ',
            'د پیسو تادیه او واستلو شیوه غوره کړئ',
            'محصول تر لاسه ورکړئ او بې‌نظیر تجربه لذت ونیسئ'
        ]
    },
    'uz': {
        'title': "Do'kon",
        'about_title': 'Mahsulotlar Haqida',
        'about_text': "Mahsulotlarimiz go'zallikni texnologiya bilan birlashtiradi. Har bir mahsulot NFC chip bilan jihozlangan bo'lib, telefoningizga tegishingiz bilan muqaddas joylar olamini ochadi.",
        'products_title': 'Mahsulotlar',
        'product_keychain': 'NFC Kalitxona',
        'product_keychain_desc': "Islomiy naqshlar bilan chiroyli dizayn, NFC chip bilan",
        'product_card': 'NFC Karta',
        'product_card_desc': "To'g'ridan-to'g'ri ilova kirish uchun kompakt NFC karta",
        'product_phone': "NFC Telefon Qopqog'i",
        'product_phone_desc': "Ichki NFC chip bilan mos telefon qopqog'i",
        'contact_title': "Sotuvchilar Bilan Bog'lanish",
        'how_title': 'Mahsulotni Qanday Olish Mumkin',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            "Rasmiy do'konlardan to'g'ri mahsulotni tanlang",
            "WhatsApp yoki email orqali sotuvchi bilan bog'laning",
            "To'lov va yetkazib berish usulini tanlang",
            "Mahsulotni oling va noyob tajribadan bahramand bo'ling"
        ]
    },
    'ru': {
        'title': 'Магазин',
        'about_title': 'О Продуктах',
        'about_text': 'Наши продукты сочетают красоту и технологии. Каждый продукт оснащен NFC-чипом, который открывает мир Священных мест при касании телефона.',
        'products_title': 'Продукты',
        'product_keychain': 'NFC Брелок',
        'product_keychain_desc': 'Элегантный дизайн с исламскими узорами, оснащен NFC-чипом',
        'product_card': 'NFC Карта',
        'product_card_desc': 'Компактная карта с NFC-чипом для прямого доступа',
        'product_phone': 'NFC Чехол',
        'product_phone_desc': 'Совместимый чехол со встроенным NFC-чипом',
        'contact_title': 'Связаться с Продавцами',
        'how_title': 'Как Получить Продукт',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Выберите подходящий продукт в авторизованных магазинах',
            'Свяжитесь с продавцом через WhatsApp или email',
            'Выберите способ оплаты и доставки',
            'Получите продукт и наслаждайтесь уникальным опытом'
        ]
    },
    'zh': {
        'title': '商店',
        'about_title': '关于产品',
        'about_text': '我们的产品将美丽与科技相结合。每个产品都配备NFC芯片，当您用手机触碰时，即可打开圣地的世界。优雅耐用的设计使其成为热爱圣地之人的完美礼物。',
        'products_title': '产品',
        'product_keychain': 'NFC钥匙链',
        'product_keychain_desc': '伊斯兰花纹的优雅设计，配备NFC芯片',
        'product_card': 'NFC卡片',
        'product_card_desc': '紧凑的NFC卡片，可直接访问应用',
        'product_phone': 'NFC手机壳',
        'product_phone_desc': '兼容各种设备，内置NFC芯片',
        'contact_title': '联系卖家',
        'how_title': '如何获取产品',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': '电子邮件', 'value': 'info@haramain.com'}
        ],
        'steps': [
            '从授权商店选择合适的产品',
            '通过WhatsApp或电子邮件联系卖家',
            '选择合适的支付和配送方式',
            '收到产品，享受独特体验'
        ]
    },
    'az': {
        'title': 'Ma\u011faza',
        'about_title': 'M\u0259hsullar Haqq\u0131nda',
        'about_text': 'M\u0259hsullar\u0131m\u0131z g\u00f6z\u0259llikl\u0259 texnologiyan\u0131 birl\u015e\u015ftirir. H\u0259r m\u0259hsul NFC \u00e7ip il\u0259 t\u0259chiz olunub ki, telefonunuza toxunduqda m\u00fcq\u0259dd\u0259s yerl\u0259rin d\u00fcnyas\u0131n\u0131 a\u00e7\u0131r.',
        'products_title': 'M\u0259hsullar',
        'product_keychain': 'NFC A\u00e7arl\u0131q',
        'product_keychain_desc': '\u0130slam nax\u0131\u015f\u0131 il\u0259 z\u0259rif dizayn, NFC \u00e7ipli',
        'product_card': 'NFC Kart',
        'product_card_desc': 'Birba\u015fa t\u0259tbiq giri\u015fi \u00fcch\u00fcn kompakt NFC kart',
        'product_phone': 'NFC Telefon Qab\u0131',
        'product_phone_desc': 'Daxili NFC \u00e7ip il\u0259 uygun telefon qab\u0131',
        'contact_title': 'Sat\u0131c\u0131larla \u0130laq\u0259',
        'how_title': 'M\u0259hsulu Nec\u0259 Almaq Olar',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Sertifikatl\u0131 ma\u011fazalardan uygun m\u0259hsulu se\u00e7in',
            'WhatsApp v\u0259 ya email vasit\u0259sil\u0259 sat\u0131c\u0131 il\u0259 \u0130laq\u0259 saxlay\u0131n',
            '\u00d6d\u0259ni\u015f v\u0259 \u00e7atd\u0131r\u0131lma metodunu se\u00e7in',
            'M\u0259hsulunuzu al\u0131n v\u0259 unikal t\u0259cr\u00fcbc\u0259d\u0259n z\u00f6vq al\u0131n'
        ]
    },
    'ku': {
        'title': 'D\u00eekan',
        'about_title': 'Derbar\u00ea Productan',
        'about_text': 'Productan me h\u00fbn\u00een\u00ee le di technology\u00ea de t\u0259kild\u00eene. Her product de \u00e7\u00eepa NFC heye ku di h\u0259san\u00ea bi telefon\u00ea re dunyaya Qutbulxaniman ve dike.',
        'products_title': 'Productan',
        'product_keychain': 'Guhertina Mifte\u00ear\u00ea NFC',
        'product_keychain_desc': 'Nim\u00fbney\u00ean \u0130slam\u00ee bi endamaya nerm, bi \u00e7\u00eepa NFC re',
        'product_card': 'Karta NFC',
        'product_card_desc': 'Karta compact bi \u00e7\u00eepa NFC re ji bo gih\u00ee\u015ftina rast\u00ee',
        'product_phone': 'Qoba T\u00e9l\u00e9fona NFC',
        'product_phone_desc': 'Qoba hevgirt\u00ee bi \u00e7\u00eepa NFC re',
        'contact_title': 'T\u0259kiliya Firot\u00eeyan',
        'how_title': '\u00c7awa Dibe Product B\u00een\u00ee',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Producta away\u00ee ji dik\u00ean\u00ean bi nav nas kir\u00een \u00eax\u00eene',
            'Bi WhatsApp an email re bi firot\u00eeyan t\u0259kiliya b\u00eene',
            'Away\u00ee p\u0259\u015fdr\u00eedan \u00fb seferkirin\u00ea \u00eax\u00eene',
            'Producta xwe bist\u00eene \u00fb tec\u00fbrbeya taybet\u00ee hej\u00een b\u00eene'
        ]
    },
    'so': {
        'title': 'Dukaan',
        'about_title': 'Ku Saabsan Alaabta',
        'about_text': 'Alaabtayadu waxay isku daraysaa qurux iyo teknoloji. Alaab kasta waxay leedahay NFC chip oo furaysa adduunka Meelaha Quruxda badan markaad taabatay telefoonkaaga.',
        'products_title': 'Alaabta',
        'product_keychain': 'Furaha NFC',
        'product_keychain_desc': 'Naqshad qurux badan oo Islaami ah, leh NFC chip',
        'product_card': 'Kaarka NFC',
        'product_card_desc': 'Kaar yar oo leh NFC chip si toos ah loogu galo app-ka',
        'product_phone': 'Daboolka Taleefanka NFC',
        'product_phone_desc': 'Dabool iswaafajiya oo leh NFC chip gudaheeda',
        'contact_title': 'La Xiriir Diiyaariyayaasha',
        'how_title': 'Sida Loo Helo Alaabta',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Dooro alaabta ku habboon dukaamada rasmiga ah',
            'La xiriir diiwaariyaha WhatsApp ama email',
            'Dooro habka lacag bixinta iyo shipping-ka',
            'Ku qaado alaabtaada oo ku raaxayso khibrad gaar ah'
        ]
    },
    'bs': {
        'title': 'Prodavnica',
        'about_title': 'O Proizvodima',
        'about_text': 'Na\u0161i proizvodi spajaju ljepotu i tehnologiju. Svaki proizvod ima NFC \u010dip koji otvara svet Svetih mesta kada dodirnete telefon.',
        'products_title': 'Proizvodi',
        'product_keychain': 'NFC Privesak',
        'product_keychain_desc': 'Elegantan dizajn sa islamskim motivima, sa NFC \u010dipom',
        'product_card': 'NFC Kartica',
        'product_card_desc': 'Kompaktna kartica sa NFC \u010dipom za direktan pristup',
        'product_phone': 'NFC Maskica',
        'product_phone_desc': 'Kompatibilna maskica sa ugra\u0111enim NFC \u010dipom',
        'contact_title': 'Kontaktirajte Prodava\u010de',
        'how_title': 'Kako Dobiti Proizvod',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            'Odaberite odgovaraju\u0107i proizvod iz ovla\u0161\u0107enih prodavnica',
            'Kontaktirajte prodava\u010da putem WhatsApp-a ili email-a',
            'Odaberite na\u010dina pla\u0107anja i isporuke',
            'Preuzmite proizvod i u\u017eivajte u jedinstvenom iskustvu'
        ]
    },
    'tg': {
        'title': '\u0414\u04b3\u043a\u043e\u043d',
        'about_title': '\u0414\u0430\u0440 \u0431\u043e\u0440\u0430\u0438 \u043c\u0430\u0445\u0441\u0443\u043b\u043e\u0442',
        'about_text': '\u041c\u0430\u0445\u0441\u0443\u043b\u043e\u0442\u0438 \u043c\u043e \u0437\u0435\u0431\u043e\u0438\u0439 \u0432\u0430 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u044f\u0440\u043e \u044f\u043a\u04b1\u043e\u043d\u0430 \u043c\u0435\u043a\u0443\u043d\u0430\u0434. \u0414\u0430\u0440 \u044f\u043a \u043c\u0430\u0445\u0441\u0443\u043b\u043e\u0442 \u0431\u043e \u0447\u0438\u043f\u0438 NFC \u043c\u0443\u0436\u0430\u0445\u0445\u0430\u0437 \u0430\u0441\u0442, \u043a\u0435 \u0431\u043e \u043b\u0430\u043c\u0441 \u043a\u0430\u0440\u0434\u0430\u043d\u0438 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0438 \u0448\u0443\u043c\u043e \u043e\u043b\u0430\u043c\u0438 \u04b3\u0430\u043c\u043e\u0432\u0446 \u0434\u0438\u0445\u043e\u044d\u0434 \u043c\u0435\u043a\u0443\u043d\u0430\u0434.',
        'products_title': '\u041c\u0430\u0445\u0441\u0443\u043b\u043e\u0442',
        'product_keychain': '\u041a\u0430\u043b\u0438\u0434\u0431\u0430\u043d\u0434\u0438 NFC',
        'product_keychain_desc': '\u0422\u0430\u0440\u0445\u0438 \u0437\u0435\u0431\u043e \u0431\u043e \u043d\u0430\u043c\u0443\u043d\u0430\u0445\u043e\u0438 \u0438\u0441\u043b\u043e\u043c\u0438, \u0431\u043e \u0447\u0438\u043f\u0438 NFC',
        'product_card': '\u041a\u0430\u0440\u0442\u0430\u0438 NFC',
        'product_card_desc': '\u041a\u0430\u0440\u0442\u0430\u0438 \u0445\u0443\u0440\u0434 \u0431\u043e \u0447\u0438\u043f\u0438 NFC \u0431\u0430\u0440\u043e\u0438 \u043c\u0443\u0441\u0442\u0430\u0441\u043a\u0438\u043c',
        'product_phone': '\u041f\u04b3\u0448\u0438 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0438 NFC',
        'product_phone_desc': '\u041f\u04b3\u0448\u0438 \u043c\u0443\u0432\u043e\u0444\u0438\u0441 \u0431\u043e \u0447\u0438\u043f\u0438 NFC-\u0438 \u0434\u043e\u0445\u0438\u043b\u0438',
        'contact_title': '\u0422\u0430\u043c\u043e\u0441 \u0431\u043e \u0444\u0443\u0440\u04b3\u0448\u0430\u043d\u0434\u0430\u0433\u043e\u043d',
        'how_title': '\u0427\u0438 \u0442\u0430\u0432\u0440 \u043c\u0430\u0445\u0441\u0443\u043b\u043e\u0442\u0440\u043e \u0433\u0438\u0440\u0438\u0444\u0442\u0430\u043d \u043c\u0443\u043c\u043a\u0438\u043d \u0430\u0441\u0442',
        'contacts': [
            {'label': 'WhatsApp', 'value': '+966500000000'},
            {'label': 'Email', 'value': 'info@haramain.com'}
        ],
        'steps': [
            '\u041c\u0430\u0445\u0441\u0443\u043b\u043e\u0442\u0438 \u043c\u0443\u0432\u043e\u0444\u0438\u0441\u0440\u043e \u0430\u0437 \u0434\u04b3\u043a\u043e\u043d\u04b3\u043e\u0438 \u0440\u0430\u0441\u043c\u0438 \u0438\u043d\u0442\u0438\u0445\u043e\u0431 \u043a\u0443\u043d\u0435\u0434',
            '\u0411\u043e WhatsApp \u044f\u043e email \u0442\u0430\u0432\u0430\u0441\u0441\u0443\u0440\u043e\u0438 \u0444\u0443\u0440\u04b3\u0448\u0430\u043d\u0434\u0430 \u0442\u0430\u043c\u043e\u0441 \u0433\u0438\u0440\u0435\u0444\u0435\u0434',
            '\u0423\u0441\u0443\u043b\u0438 \u043f\u0430\u0440\u0434\u043e\u0445\u0442 \u0432\u0430 \u0438\u043d\u0442\u0438\u0445\u043e\u043b\u0438 \u0440\u043e \u0438\u043d\u0442\u0438\u0445\u043e\u043b \u043a\u0443\u043d\u0435\u0434',
            '\u041c\u0430\u0445\u0441\u0443\u043b\u043e\u0442\u0440\u043e \u0433\u0438\u0440\u0435\u0444\u0435\u0434 \u0432\u0430 \u0430\u0437 \u0442\u0430\u04b3\u0440\u0438\u0431\u0430\u0438 \u0431\u0435\u043d\u0430\u0437\u0438\u0440 \u0431\u0430\u0440\u0435\u0434'
        ]
    }
}

for lang, data in translations.items():
    filepath = f'public/lang/{lang}.json'
    with open(filepath, 'r') as f:
        file_data = json.load(f)
    file_data['shop'] = data
    with open(filepath, 'w') as f:
        json.dump(file_data, f, ensure_ascii=False, indent=2)
    print(f'Updated {lang}.json')
print('Done!')
