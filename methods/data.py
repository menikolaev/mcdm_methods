criteria_data = {
    'high_level': [
        ['I1', '1 / I6', 'I5', '1 / I2', '1 / I3', '1 / I3', '1 / I7', 'I3', '1 / I4'],
        ['I6', 'I1', 'I7', 'I2', 'I6', '1 / I2', 'I4', 'I3', '1 / I3'],
        ['1 / I5', '1 / I7', 'I1', '1 / I6', '1 / I7', '1 / I8', '1 / I4', '1 / I2', '1 / I9'],
        ['I2', '1 / I2', 'I6', 'I1', 'I2', '1 / I5', '1 / I3', 'I2', '1 / I7'],
        ['I3', '1 / I6', 'I7', '1 / I2', 'I1', '1 / I4', '1 / I2', 'I5', '1 / I6'],
        ['I3', 'I2', 'I8', 'I5', 'I4', 'I1', 'I4', 'I6', '1 / I2'],
        ['I7', '1 / I4', 'I4', 'I3', 'I2', '1 / I4', 'I1', 'I3', '1 / I5'],
        ['1 / I3', '1 / I3', 'I2', '1 / I2', '1 / I5', '1 / I6', '1 / I3', 'I1', '1 / I7'],
        ['I4', 'I3', 'I9', 'I7', 'I6', 'I2', 'I5', 'I7', 'I1'],
    ],
    'subcriteria': {
        'UTM': {
            'high_level': [
                ['I1', '1 / I3', '1 / I5'],
                ['I3', 'I1', '1 / I3'],
                ['I5', 'I3', 'I1'],
            ]
        },
        'Functionality': {
            'high_level': [
                ['I1', '1 / I5'],
                ['I5', 'I1'],
            ]
        },
        'Strategic factors': {
            'high_level': [
                ['I1', 'I4', 'I3'],
                ['1 / I4', 'I1', 'I2'],
                ['1 / I3', '1 / I2', 'I1'],
            ]
        }
    }
}

data = {
    'Performance': [
        ['E1', 'E3', '1 / E2', '1 / E4'],
        ['1 / E3', 'E1', '1 / E5', '1 / E7'],
        ['E2', 'E5', 'E1', '1 / E3'],
        ['E4', 'E7', 'E3', 'E1'],
    ],
    'Web filtering': [
        ['E1', '1 / E3', '1 / E6', 'E2'],
        ['E3', 'E1', '1 / E3', 'E5'],
        ['E6', 'E3', 'E1', 'E8'],
        ['1 / E2', '1 / E5', '1 / E8', 'E1'],
    ],
    'Antivirus': [
        ['E1', '1 / E2', '1 / E4', '1 / E7'],
        ['E2', 'E1', '1 / E3', '1 / E5'],
        ['E4', 'E3', 'E1', '1 / E4'],
        ['E7', 'E5', 'E4', 'E1'],
    ],
    'IDS/IPS': [
        ['E1', '1 / E5', '1 / E6', '1 / E5'],
        ['E5', 'E1', '1 / E3', '1 / E2'],
        ['E6', 'E3', 'E1', 'E3'],
        ['E5', 'E2', '1 / E3', 'E1'],
    ],
    'Management': [
        ['E1', '1 / E3', '1 / E9', '1 / E2'],
        ['E3', 'E1', '1 / E6', 'E2'],
        ['E9', 'E6', 'E1', 'E8'],
        ['E2', '1 / E2', '1 / E8', 'E1'],
    ],
    'Networking': [
        ['E1', 'E3', 'E2', 'E5'],
        ['1 / E3', 'E1', '1 / E3', 'E3'],
        ['1 / E2', 'E3', 'E1', 'E6'],
        ['1 / E5', '1 / E3', '1 / E6', 'E1'],
    ],
    'Completeness': [
        ['E1', 'E4', 'E2', 'E6'],
        ['1 / E4', 'E1', '1 / E3', 'E4'],
        ['1 / E2', 'E3', 'E1', 'E5'],
        ['1 / E6', '1 / E4', '1 / E5', 'E1'],
    ],
    'Correctness': [
        ['E1', 'E2', '1 / E3', '1 / E5'],
        ['1 / E2', 'E1', '1 / E4', '1 / E7'],
        ['E3', 'E4', 'E1', '1 / E3'],
        ['E5', 'E7', 'E3', 'E1'],
    ],
    'Security': [
        ['E1', 'E4', '1 / E3', '1 / E2'],
        ['1 / E4', 'E1', '1 / E4', '1 / E3'],
        ['E3', 'E4', 'E1', 'E2'],
        ['E2', 'E3', '1 / E2', 'E1'],
    ],
    'Efficiency': [
        ['E1', '1 / E3', '1 / E3', 'E2'],
        ['E3', 'E1', '1 / E2', 'E3'],
        ['E3', 'E2', 'E1', 'E5'],
        ['1 / E2', '1 / E3', '1 / E5', 'E1'],
    ],
    'Maintainability': [
        ['E1', 'E4', '1 / E3', 'E5'],
        ['1 / E4', 'E1', '1 / E4', '1 / E2'],
        ['E3', 'E4', 'E1', 'E3'],
        ['1 / E5', 'E2', '1 / E3', 'E1'],
    ],
    'Vendor capabilities': [
        ['E1', 'E3', '1 / E4', '1 / E3'],
        ['1 / E3', 'E1', '1 / E5', '1 / E3'],
        ['E4', 'E5', 'E1', 'E2'],
        ['E3', 'E3', '1 / E2', 'E1'],
    ],
    'Business issues': [
        ['E1', 'E4', 'E2', 'E3'],
        ['1 / E4', 'E1', '1 / E3', '1 / E2'],
        ['1 / E2', 'E3', 'E1', 'E2'],
        ['1 / E3', 'E2', '1 / E2', 'E1'],
    ],
    'Cost': [
        ['E1', '1 / E4', 'E5', '1 / E2'],
        ['E4', 'E1', 'E7', 'E3'],
        ['1 / E5', '1 / E7', 'E1', '1 / E3'],
        ['E2', '1 / E3', 'E3', 'E1'],
    ]
}

alternatives = ['Cisco ASAv', 'Juniper vSRX', 'Fortigate VMX NGFW', 'Palo Alto VM-Series']

criteria_hierarchy = {
    'Performance': 'Performance',
    'UTM': [
        'Web filtering',
        'Antivirus',
        'IDS/IPS',
    ],
    'Management': 'Management',
    'Networking': 'Networking',
    'Functionality': [
        'Completeness',
        'Correctness',
    ],
    'Security': 'Security',
    'Efficiency': 'Efficiency',
    'Maintainability': 'Maintainability',
    'Strategic factors': [
        'Vendor capabilities',
        'Business issues',
        'Cost'
    ]

}

high_level_criteria = [
    'Performance', 'UTM', 'Management', 'Networking', 'Functionality', 'Security', 'Efficiency', 'Maintainability',
    'Strategic factors'
]
