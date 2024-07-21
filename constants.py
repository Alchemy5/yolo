"""
List of 50 stocks per sector for avg purposes.
"""

STOCKS = {
    'Technology': [
        'AAPL',  # Apple Inc.
        'MSFT',  # Microsoft Corporation
        'GOOGL', # Alphabet Inc. (Class A)
        'GOOG',  # Alphabet Inc. (Class C)
        'AMZN',  # Amazon.com, Inc.
        'FB',    # Meta Platforms, Inc. (formerly Facebook)
        'NVDA',  # NVIDIA Corporation
        'TSLA',  # Tesla, Inc.
        'INTC',  # Intel Corporation
        'CSCO',  # Cisco Systems, Inc.
        'ORCL',  # Oracle Corporation
        'IBM',   # International Business Machines Corporation
        'SAP',   # SAP SE
        'ADBE',  # Adobe Inc.
        'AVGO',  # Broadcom Inc.
        'TXN',   # Texas Instruments Incorporated
        'QCOM',  # QUALCOMM Incorporated
        'MU',    # Micron Technology, Inc.
        'AMAT',  # Applied Materials, Inc.
        'NOK',   # Nokia Corporation
        'STX',   # Seagate Technology Holdings PLC
        'WDC',   # Western Digital Corporation
        'TSM',   # Taiwan Semiconductor Manufacturing Company
        'SHOP',  # Shopify Inc.
        'SNPS',  # Synopsys, Inc.
        'CDNS',  # Cadence Design Systems, Inc.
        'HPE',   # Hewlett Packard Enterprise Company
        'FISV',  # Fiserv, Inc.
        'LRCX',  # Lam Research Corporation
        'PANW',  # Palo Alto Networks, Inc.
        'ZM',    # Zoom Video Communications, Inc.
        'DOCU',  # DocuSign, Inc.
        'TWLO',  # Twilio Inc.
        'MS',    # Morgan Stanley (Tech-focused financials)
        'BIDU',  # Baidu, Inc.
        'JD',    # JD.com, Inc.
        'MELI',  # MercadoLibre, Inc.
        'RBLX',  # Roblox Corporation
        'SHOP',  # Shopify Inc.
        'FIVN',  # Five9, Inc.
        'GPN',   # Global Payments Inc.
        'KLA',   # KLA Corporation
        'HUBS',  # HubSpot, Inc.
        'PINS',  # Pinterest, Inc.
        'U',     # Unity Software Inc.
        'ASML',  # ASML Holding N.V.
        'ROKU',  # Roku, Inc.
        'TDD',   # Tenet Healthcare Corporation (Tech-focused healthcare)
        'DT',    # Dynatrace, Inc.
        'ZS',    # Zscaler, Inc.
        'NET',   # Cloudflare, Inc.
        'TEAM',  # Atlassian Corporation Plc
        'CLOU',  # Veeva Systems Inc.
        'RNG',   # RingCentral, Inc.
        'RDSA',  # Royal Dutch Shell plc (Tech-focused energy)
        'LVS',   # Las Vegas Sands Corp. (Tech-focused travel and leisure)
    ],

    'Consumer Cyclical': [
        'AMZN',  # Amazon.com, Inc.
        'TSLA',  # Tesla, Inc.
        'MCD',   # McDonald's Corporation
        'NKE',   # Nike, Inc.
        'DIS',   # The Walt Disney Company
        'HD',    # The Home Depot, Inc.
        'LOW',   # Lowe's Companies, Inc.
        'CMG',   # Chipotle Mexican Grill, Inc.
        'STAR',  # Starwood Property Trust, Inc.
        'BABA',  # Alibaba Group Holding Limited
        'JD',    # JD.com, Inc.
        'SBUX',  # Starbucks Corporation
        'PZZA',  # Papa John's International, Inc.
        'YUM',   # Yum! Brands, Inc.
        'DPZ',   # Domino's Pizza, Inc.
        'LVS',   # Las Vegas Sands Corp.
        'WYNN',  # Wynn Resorts, Limited
        'MGM',   # MGM Resorts International
        'RCL',   # Royal Caribbean Cruises Ltd.
        'CCL',   # Carnival Corporation
        'HIL',   # Hillenbrand, Inc.
        'GPC',   # Genuine Parts Company
        'BBY',   # Best Buy Co., Inc.
        'TGT',   # Target Corporation
        'WMT',   # Walmart Inc.
        'KSS',   # Kohl's Corporation
        'GPS',   # Gap, Inc.
        'RL',    # Ralph Lauren Corporation
        'COH',   # Coach, Inc.
        'FOSL',  # Fossil Group, Inc.
        'LULU',  # Lululemon Athletica Inc.
        'ZUMZ',  # Zumiez Inc.
        'HBI',   # Hanesbrands Inc.
        'PVH',   # PVH Corp.
        'TIF',   # Tiffany & Co.
        'KMX',   # CarMax, Inc.
        'AZO',   # AutoZone, Inc.
        'ORLY',  # O'Reilly Automotive, Inc.
        'AAP',   # Advance Auto Parts, Inc.
        'M',     # Macy's, Inc.
        'JWN',   # Nordstrom, Inc.
        'HOG',   # Harley-Davidson, Inc.
        'F',     # Ford Motor Company
        'GM',    # General Motors Company
        'NVR',   # NVR, Inc.
        'LEN',   # Lennar Corporation
        'DHI',   # D.R. Horton, Inc.
        'PHM',   # PulteGroup, Inc.
        'RCL',   # Royal Caribbean Group
        'LVS',   # Las Vegas Sands Corp.
        'BBBY',  # Bed Bath & Beyond Inc.
        'PCLN',  # Booking Holdings Inc. (formerly Priceline)
        'WAB',   # Wabtec Corporation
    ],
    'Healthcare': [
        'JNJ',   # Johnson & Johnson
        'PFE',   # Pfizer Inc.
        'MRK',   # Merck & Co., Inc.
        'ABBV',  # AbbVie Inc.
        'AMGN',  # Amgen Inc.
        'GILD',  # Gilead Sciences, Inc.
        'BIIB',  # Biogen Inc.
        'VRTX',  # Vertex Pharmaceuticals Incorporated
        'REGN',  # Regeneron Pharmaceuticals, Inc.
        'BMY',   # Bristol-Myers Squibb Company
        'MDT',   # Medtronic plc
        'SYK',   # Stryker Corporation
        'ABT',   # Abbott Laboratories
        'DHR',   # Danaher Corporation
        'ISRG',  # Intuitive Surgical, Inc.
        'ELV',   # Elevance Health, Inc. (formerly Anthem, Inc.)
        'CVS',   # CVS Health Corporation
        'UNH',   # UnitedHealth Group Incorporated
        'HCA',   # HCA Healthcare, Inc.
        'Lilly', # Eli Lilly and Company
        'CNC',   # Centene Corporation
        'BAX',   # Baxter International Inc.
        'GSK',   # GlaxoSmithKline plc
        'NVO',   # Novo Nordisk A/S
        'AZN',   # AstraZeneca PLC
        'HUM',   # Humana Inc.
        'RMD',   # ResMed Inc.
        'ZTS',   # Zoetis Inc.
        'MCK',   # McKesson Corporation
        'ORLY',  # O'Reilly Automotive, Inc. (Healthcare-related services)
        'HST',   # Host Hotels & Resorts, Inc. (Healthcare REIT)
        'WBA',   # Walgreens Boots Alliance, Inc.
        'SNY',   # Sanofi
        'PODD',  # Insulet Corporation
        'ILMN',  # Illumina, Inc.
        'MTD',   # Mettler-Toledo International Inc.
        'CRL',   # Charles River Laboratories International, Inc.
        'RGEN',  # Repligen Corporation
        'CDNA',  # CareDx, Inc.
        'TMO',   # Thermo Fisher Scientific Inc.
        'BMRN',  # BioMarin Pharmaceutical Inc.
        'ICUI',  # ICU Medical, Inc.
        'MASI',  # Masimo Corporation
        'PRGO',  # Perrigo Company plc
        'IDXX',  # IDEXX Laboratories, Inc.
        'NVS',   # Novartis AG
        'SGEN',  # Seagen Inc.
        'KRTX',  # Karuna Therapeutics, Inc.
        'NTRA',  # Natera, Inc.
        'ALXN',  # Alexion Pharmaceuticals, Inc.
        'STJ',   # St. Jude Medical, Inc. (now part of Abbott Laboratories)
        'UHS',   # Universal Health Services, Inc.
        'GILD',  # Gilead Sciences, Inc.
    ],
    'Industrials': [
        'BA',    # Boeing Company
        'CAT',   # Caterpillar Inc.
        'DE',    # Deere & Company
        'HON',   # Honeywell International Inc.
        'GE',    # General Electric Company
        'UPS',   # United Parcel Service, Inc.
        'FedEx', # FedEx Corporation
        '3M',    # 3M Company
        'LMT',   # Lockheed Martin Corporation
        'RTX',   # Raytheon Technologies Corporation
        'EMR',   # Emerson Electric Co.
        'DOV',   # Dover Corporation
        'FLIR',  # FLIR Systems, Inc.
        'TMO',   # Thermo Fisher Scientific Inc. (also in Healthcare)
        'FLS',   # Flowserve Corporation
        'NOC',   # Northrop Grumman Corporation
        'GD',    # General Dynamics Corporation
        'CARR',  # Carrier Global Corporation
        'LUV',   # Southwest Airlines Co.
        'DAL',   # Delta Air Lines, Inc.
        'UAL',   # United Airlines Holdings, Inc.
        'CSX',   # CSX Corporation
        'NSC',   # Norfolk Southern Corporation
        'UNP',   # Union Pacific Corporation
        'XPO',   # XPO Logistics, Inc.
        'LUV',   # Southwest Airlines Co.
        'UAL',   # United Airlines Holdings, Inc.
        'PWR',   # Quanta Services, Inc.
        'RCL',   # Royal Caribbean Cruises Ltd.
        'HII',   # Huntington Ingalls Industries, Inc.
        'ITW',   # Illinois Tool Works Inc.
        'LII',   # Lennox International Inc.
        'CMI',   # Cummins Inc.
        'SNA',   # Snap-on Incorporated
        'MAS',   # Masco Corporation
        'HOG',   # Harley-Davidson, Inc.
        'JCI',   # Johnson Controls International plc
        'ECL',   # Ecolab Inc.
        'RHI',   # Robert Half International Inc.
        'TTEK',  # Tetra Tech, Inc.
        'PNR',   # Pentair plc
        'ABM',   # ABM Industries Incorporated
        'DHR',   # Danaher Corporation (also in Healthcare)
        'KMT',   # Kennametal Inc.
        'AVY',   # Avery Dennison Corporation
        'STLD',  # Steel Dynamics, Inc.
        'TRN',   # Trinity Industries, Inc.
        'GWW',   # Grainger (W.W.) Inc.
        'FAST',  # Fastenal Company
        'VMI',   # Valmont Industries, Inc.
        'TSCO',  # Tractor Supply Company
        'PWR',   # Quanta Services, Inc.
        'WAB',   # Wabtec Corporation
    ],
    'Utilities' : [
        'DUK',   # Duke Energy Corporation
        'NEE',   # NextEra Energy, Inc.
        'D',     # Dominion Energy, Inc.
        'SO',    # The Southern Company
        'XEL',   # Xcel Energy Inc.
        'PEG',   # Public Service Enterprise Group Incorporated
        'ED',    # Consolidated Edison, Inc.
        'CMS',   # CMS Energy Corporation
        'AEP',   # American Electric Power Company, Inc.
        'ES',    # Eversource Energy
        'WEC',   # WEC Energy Group, Inc.
        'SRE',   # Sempra Energy
        'PPL',   # PPL Corporation
        'AWK',   # American Water Works Company, Inc.
        'AEE',   # Ameren Corporation
        'NWE',   # NorthWestern Corporation
        'XEL',   # Xcel Energy Inc.
        'SNP',   # China Petroleum & Chemical Corporation (Sinopec)
        'EIX',   # Edison International
        'LNT',   # Alliant Energy Corporation
        'NFG',   # National Fuel Gas Company
        'NWN',   # Northwest Natural Holding Company
        'TRP',   # TC Energy Corporation
        'CNP',   # CenterPoint Energy, Inc.
        'EQT',   # EQT Corporation
        'WTRG',  # Aqua America, Inc.
        'NRG',   # NRG Energy, Inc.
        'RNG',   # RingCentral, Inc. (utilities-related services)
        'PBA',   # Pembina Pipeline Corporation
        'VST',   # Vistra Corp.
        'ZAYO',  # Zayo Group Holdings, Inc.
        'HST',   # Host Hotels & Resorts, Inc. (utilities-related REIT)
        'PPL',   # PPL Corporation
        'VLO',   # Valero Energy Corporation (utilities-related services)
        'GLNG',  # Golar LNG Limited
        'TRP',   # TC Energy Corporation
        'DTE',   # DTE Energy Company
        'NEE',   # NextEra Energy, Inc.
        'FTS',   # Fortis Inc.
        'ENB',   # Enbridge Inc.
        'VST',   # Vistra Corp.
        'BEP',   # Brookfield Renewable Partners L.P.
        'BIP',   # Brookfield Infrastructure Partners L.P.
        'KMI',   # Kinder Morgan, Inc.
        'LNT',   # Alliant Energy Corporation
        'ENI',   # Eni S.p.A. (utilities-related services)
        'AEE',   # Ameren Corporation
        'HST',   # Host Hotels & Resorts, Inc. (utilities-related REIT)
        'BXP',   # Boston Properties, Inc. (utilities-related REIT)
        'CLX',   # The Clorox Company (utilities-related services)
    ]
}