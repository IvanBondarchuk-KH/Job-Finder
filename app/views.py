from django.shortcuts import render

vacancies = [
    {
        'id': 1,
        'title': 'AI Research Scientist',
        'company': 'Google DeepMind',
        'salary': '15000$',
        'description': 'Developing and training new artificial intelligence models. Working on the creation of Artificial General Intelligence (AGI) and improving future large language models. Requires deep knowledge of mathematics, neural networks, and experience with Python, PyTorch, or TensorFlow.'
    },
    {
        'id': 2,
        'title': 'Robotics Software Engineer',
        'company': 'Google X (The Moonshot Factory)',
        'salary': '14200$',
        'description': 'Programming and testing software for secret robotics projects. Creating algorithms for autonomous movement, navigation, and human-robot interaction. Uses C++ and Python languages, as well as ROS (Robot Operating System).'
    },
    {
        'id': 3,
        'title': 'Quantum Computing Engineer',
        'company': 'IBM Quantum',
        'salary': '13500$',
        'description': 'Project work in the field of quantum computing. Writing algorithms for quantum computers, optimizing existing systems, and running tests on real quantum hardware. Working with the Qiskit framework and conducting scientific research.'
    },
    {
        'id': 4,
        'title': 'Spacecraft Software Engineer',
        'company': 'SpaceX',
        'salary': '12800$',
        'description': 'Developing mission-critical software for Falcon rockets and Dragon spacecraft flight computers. Writing code for flight control systems, telemetry, and astronaut safety. Requires perfect knowledge of C++ and experience with Linux systems.'
    },
    {
        'id': 5,
        'title': 'Self-Driving Software Engineer',
        'company': 'Tesla',
        'salary': '13000$',
        'description': 'Working on the Full Self-Driving (FSD) autopilot system. Writing computer vision algorithms to recognize road signs, lane markings, and pedestrians in real time. Processing gigabytes of video data using artificial intelligence.'
    },
    {
        'id': 6,
        'title': 'Cybersecurity Architect',
        'company': 'Microsoft',
        'salary': '11500$',
        'description': 'Designing secure cloud systems and protecting global infrastructure from hacker attacks. Finding vulnerabilities in code, creating data encryption systems, and responding quickly to cyber threats. Requires a deep understanding of network architecture.'
    },
    {
        'id': 7,
        'title': 'Cloud Infrastructure Engineer',
        'company': 'Amazon Web Services (AWS)',
        'salary': '11000$',
        'description': 'Supporting and developing the world’s largest cloud platform. Creating tools for automatic server scaling and optimizing website access speeds globally. Working with Docker, Kubernetes, and cloud architectures.'
    },
    {
        'id': 8,
        'title': 'Game Engine Developer',
        'company': 'Epic Games',
        'salary': '10500$',
        'description': 'Improving the technologies of the Unreal Engine. Developing new tools for realistic graphics, destruction physics, and optimizing games for next-generation consoles and PC. Requires professional knowledge of C++ and graphics APIs (DirectX/Vulkan).'
    },
    {
        'id': 9,
        'title': 'VR/AR Software Developer',
        'company': 'Meta',
        'salary': '12000$',
        'description': 'Creating applications and games for virtual (VR) and augmented (AR) reality headsets, such as Meta Quest. Developing 3D user interfaces, hand-tracking, and eye-tracking systems. Working within Unity or Unreal Engine environments.'
    },
    {
        'id': 10,
        'title': 'Blockchain Core Developer',
        'company': 'Ethereum Foundation',
        'salary': '12500$',
        'description': 'Working on core network upgrades for Ethereum to improve scalability and security. Creating standards for smart contracts and decentralized applications (dApps). Requires knowledge of cryptography and programming languages like Solidity, Go, or Rust.'
    }
]

def index(request):
    context = {
        'site_title': 'Job Search',
        'vacancies': vacancies,
    }
    return render(request, 'jobs/index.html', context)

def vacancy_detail(request, vacancy_id):
    vacancy = next((v for v in vacancies if v['id'] == vacancy_id), None)
    if not vacancy:
        return render(request, 'jobs/404.html', status=404)
    context = {
        'vacancy': vacancy,
    }
    return render(request, 'jobs/detail.html', context)