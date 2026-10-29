import os
from flask import Flask, render_template_string, redirect
app = Flask(__name__)

STUDYBUDDY_URL = os.environ.get(
    "STUDYBUDDY_URL",
    "https://your-studybuddy.onrender.com"
)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Professional digital portfolio of Rhea Dumagat">
    <title>Rhea Dumagat | Digital Portfolio</title>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --bg: #08090c;
            --bg-soft: #101217;
            --card: rgba(22, 24, 31, 0.82);
            --card-solid: #15171d;
            --text: #f5f5f5;
            --muted: #a8adb8;
            --line: rgba(255,255,255,0.09);
            --accent: #b30000;
            --accent-light: #e00000;
            --accent-soft: rgba(179,0,0,0.15);
            --max: 1180px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
            scroll-padding-top: 90px;
        }

        body {
            font-family: 'Inter', Arial, sans-serif;
            background:
                radial-gradient(circle at 80% 10%, rgba(179,0,0,0.10), transparent 30%),
                radial-gradient(circle at 10% 70%, rgba(179,0,0,0.07), transparent 28%),
                var(--bg);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        .container {
            width: min(92%, var(--max));
            margin: 0 auto;
        }

        /* =========================
           ANIMATED GEOMETRIC BACKGROUND
        ========================= */

        .geometry {
            position: fixed;
            inset: 0;
            overflow: hidden;
            pointer-events: none;
            z-index: -1;
        }

        .shape {
            position: absolute;
            border: 1px solid rgba(179,0,0,0.25);
            opacity: 0.45;
        }

        .shape.one {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            top: 18%;
            left: 5%;
            animation: floatOne 13s ease-in-out infinite;
        }

        .shape.two {
            width: 75px;
            height: 75px;
            right: 7%;
            top: 28%;
            transform: rotate(45deg);
            animation: floatTwo 16s ease-in-out infinite;
        }

        .shape.three {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            border-width: 10px;
            right: 15%;
            bottom: 5%;
            opacity: 0.18;
            animation: floatThree 18s ease-in-out infinite;
        }

        .shape.four {
            width: 180px;
            height: 1px;
            left: 42%;
            top: 16%;
            transform: rotate(-30deg);
            animation: lineMove 11s ease-in-out infinite;
        }

        .shape.five {
            width: 45px;
            height: 45px;
            left: 12%;
            bottom: 15%;
            transform: rotate(45deg);
            animation: spin 12s linear infinite;
        }

        @keyframes floatOne {
            0%, 100% { transform: translate(0,0); }
            50% { transform: translate(70px,-50px); }
        }

        @keyframes floatTwo {
            0%, 100% { transform: rotate(45deg) translate(0,0); }
            50% { transform: rotate(180deg) translate(-40px,60px); }
        }

        @keyframes floatThree {
            0%,100% { transform: translate(0,0) scale(1); }
            50% { transform: translate(-50px,-40px) scale(1.15); }
        }

        @keyframes lineMove {
            0%,100% { transform: translateX(0) rotate(-30deg); }
            50% { transform: translateX(100px) rotate(-18deg); }
        }

        @keyframes spin {
            from { transform: rotate(45deg); }
            to { transform: rotate(405deg); }
        }

        /* =========================
           NAVBAR
        ========================= */

        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: rgba(8,9,12,0.78);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--line);
        }

        .nav-inner {
            min-height: 76px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .brand {
            font-size: 19px;
            font-weight: 800;
            letter-spacing: 1.5px;
        }

        .brand span {
            color: var(--accent-light);
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 26px;
        }

        .nav-links a {
            color: #d5d7dc;
            font-size: 13px;
            font-weight: 600;
            position: relative;
            padding: 8px 0;
            transition: 0.25s;
        }

        .nav-links a::after {
            content: "";
            position: absolute;
            left: 0;
            bottom: 0;
            width: 0;
            height: 2px;
            background: var(--accent-light);
            transition: 0.25s;
        }

        .nav-links a:hover,
        .nav-links a.active {
            color: white;
        }

        .nav-links a:hover::after,
        .nav-links a.active::after {
            width: 100%;
        }

        .menu-btn {
            display: none;
            border: 1px solid var(--line);
            background: transparent;
            color: white;
            border-radius: 8px;
            padding: 9px 11px;
            cursor: pointer;
            font-size: 18px;
        }

        /* =========================
           HERO
        ========================= */

        .hero {
            min-height: 100vh;
            display: grid;
            place-items: center;
            padding: 120px 0 80px;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            align-items: center;
            gap: 80px;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            color: #e7e7e7;
            background: var(--accent-soft);
            border: 1px solid rgba(179,0,0,0.28);
            border-radius: 999px;
            padding: 8px 13px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            margin-bottom: 22px;
        }

        .eyebrow-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--accent-light);
            box-shadow: 0 0 12px var(--accent-light);
        }

        .hero h1 {
            font-size: clamp(48px, 7vw, 82px);
            line-height: 0.98;
            letter-spacing: -3px;
            margin-bottom: 22px;
        }

        .hero h1 span {
            display: block;
            color: var(--accent-light);
        }

        .hero-subtitle {
            color: #e1e2e5;
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 15px;
        }

        .hero-description {
            max-width: 620px;
            color: var(--muted);
            font-size: 16px;
            line-height: 1.9;
            margin-bottom: 30px;
        }

        .hero-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 13px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 9px;
            padding: 13px 19px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 700;
            transition: 0.25s;
        }

        .btn-primary {
            background: var(--accent);
            border: 1px solid var(--accent);
        }

        .btn-primary:hover {
            background: var(--accent-light);
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(179,0,0,0.25);
        }

        .btn-outline {
            border: 1px solid #3b3e46;
            background: rgba(255,255,255,0.02);
        }

        .btn-outline:hover {
            border-color: var(--accent);
            transform: translateY(-3px);
        }

        /* =========================
           HERO PHOTO
        ========================= */

        .hero-photo-wrap {
            display: flex;
            justify-content: center;
            position: relative;
        }

        .hero-photo-ring {
            width: min(370px, 75vw);
            aspect-ratio: 1;
            border-radius: 50%;
            padding: 8px;
            background: linear-gradient(145deg, var(--accent-light), #450000 65%, #222);
            box-shadow:
                0 0 0 1px rgba(255,255,255,0.06),
                0 25px 80px rgba(0,0,0,0.55),
                0 0 60px rgba(179,0,0,0.18);
            animation: photoFloat 5s ease-in-out infinite;
        }

        .hero-photo {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            overflow: hidden;
            background: #15171d;
            border: 7px solid #0d0e12;
        }

        .hero-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        @keyframes photoFloat {
            0%,100% { transform: translateY(0); }
            50% { transform: translateY(-9px); }
        }

        /* =========================
           SECTIONS
        ========================= */

        section {
            padding: 105px 0;
        }

        .section-heading {
            margin-bottom: 48px;
        }

        .section-kicker {
            color: var(--accent-light);
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        .section-heading h2 {
            font-size: clamp(32px, 4vw, 46px);
            letter-spacing: -1.5px;
        }

        .section-heading p {
            max-width: 650px;
            color: var(--muted);
            margin-top: 12px;
        }

        /* =========================
           ABOUT / INFO
        ========================= */

        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 22px;
        }

        .card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 28px;
            backdrop-filter: blur(12px);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: rgba(179,0,0,0.45);
            box-shadow: 0 18px 50px rgba(0,0,0,0.25);
        }

        .card-title {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 17px;
            margin-bottom: 22px;
        }

        .title-icon {
            width: 38px;
            height: 38px;
            display: grid;
            place-items: center;
            border-radius: 10px;
            background: var(--accent-soft);
            color: #ff3d3d;
        }

        .title-icon svg {
            width: 19px;
            height: 19px;
            stroke: currentColor;
            fill: none;
            stroke-width: 1.8;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .info-list {
            display: grid;
            gap: 0;
        }

        .info-row {
            display: grid;
            grid-template-columns: 150px 1fr;
            gap: 20px;
            padding: 13px 0;
            border-bottom: 1px solid var(--line);
        }

        .info-row:last-child {
            border-bottom: 0;
        }

        .info-label {
            color: #858a96;
            font-size: 12px;
            font-weight: 700;
        }

        .info-value {
            color: #e5e6e9;
            font-size: 13px;
        }

        /* =========================
           FAMILY
        ========================= */

        .family-card {
            margin-top: 22px;
        }

        .siblings {
            display: flex;
            flex-wrap: wrap;
            gap: 9px;
            margin-top: 10px;
        }

        .tag {
            padding: 7px 11px;
            border: 1px solid var(--line);
            background: rgba(255,255,255,0.025);
            border-radius: 999px;
            color: #c8cad0;
            font-size: 12px;
        }

        /* =========================
           EDUCATION TIMELINE
        ========================= */

        .timeline {
            position: relative;
            max-width: 900px;
            margin: 0 auto;
        }

        .timeline::before {
            content: "";
            position: absolute;
            left: 20px;
            top: 8px;
            bottom: 8px;
            width: 1px;
            background: linear-gradient(var(--accent), rgba(179,0,0,0.1));
        }

        .timeline-item {
            position: relative;
            padding-left: 65px;
            margin-bottom: 34px;
        }

        .timeline-item:last-child {
            margin-bottom: 0;
        }

        .timeline-dot {
            position: absolute;
            left: 11px;
            top: 7px;
            width: 19px;
            height: 19px;
            border-radius: 50%;
            background: var(--bg);
            border: 4px solid var(--accent);
            box-shadow: 0 0 16px rgba(179,0,0,0.3);
        }

        .timeline-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 22px 25px;
            transition: 0.3s;
        }

        .timeline-card:hover {
            transform: translateX(6px);
            border-color: rgba(179,0,0,0.4);
        }

        .timeline-level {
            color: var(--accent-light);
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .timeline-card h3 {
            margin: 5px 0;
            font-size: 18px;
        }

        .timeline-card p {
            color: var(--muted);
            font-size: 13px;
        }

        /* =========================
           SKILLS
        ========================= */

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
        }

        .skill-card {
            background: var(--card);
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 21px;
        }

        .skill-top {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            margin-bottom: 10px;
        }

        .skill-name {
            font-size: 13px;
            font-weight: 700;
        }

        .skill-percent {
            color: var(--accent-light);
            font-size: 12px;
            font-weight: 800;
        }

        .skill-bar {
            height: 7px;
            background: #2b2e35;
            border-radius: 999px;
            overflow: hidden;
        }

        .skill-fill {
            height: 100%;
            width: 0;
            background: linear-gradient(90deg, #720000, var(--accent-light));
            border-radius: 999px;
            transition: width 1.2s ease;
        }

        .skill-note {
            color: #858a96;
            font-size: 11px;
            margin-top: 9px;
        }

        /* =========================
           PROJECTS
        ========================= */

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }

        .project-card {
            min-height: 290px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background:
                linear-gradient(145deg, rgba(179,0,0,0.08), transparent 35%),
                var(--card);
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 27px;
            transition: 0.3s;
        }

        .project-card:hover {
            transform: translateY(-7px);
            border-color: rgba(179,0,0,0.45);
        }

        .project-number {
            color: #5e626c;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 2px;
        }

        .project-card h3 {
            font-size: 20px;
            margin: 18px 0 10px;
        }

        .project-card p {
            color: var(--muted);
            font-size: 13px;
            line-height: 1.8;
        }

        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 7px;
            margin: 22px 0;
        }

        .tech {
            padding: 5px 8px;
            background: rgba(179,0,0,0.10);
            color: #e9b2b2;
            border-radius: 5px;
            font-size: 10px;
            font-weight: 700;
        }

        /* =========================
           CERTIFICATES
        ========================= */

        .certificate-card {
            min-height: 0;
        }

        .certificate-preview-link {
            display: block;
            margin: 18px 0;
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 10px;
            background: rgba(255,255,255,0.03);
        }

        .certificate-preview {
            display: block;
            width: 100%;
            aspect-ratio: 4 / 3;
            object-fit: contain;
            background: #f4f4f4;
            transition: transform 0.3s ease;
        }

        .certificate-preview-link:hover .certificate-preview {
            transform: scale(1.025);
        }

        /* =========================
           CONTACT
        ========================= */

        .contact-grid {
            display: grid;
            grid-template-columns: 0.9fr 1.1fr;
            gap: 22px;
        }

        .contact-intro {
            background:
                linear-gradient(145deg, rgba(179,0,0,0.16), transparent 55%),
                var(--card);
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 32px;
        }

        .contact-intro h3 {
            font-size: 28px;
            margin-bottom: 13px;
        }

        .contact-intro p {
            color: var(--muted);
            font-size: 13px;
            line-height: 1.9;
        }

        .contact-list {
            margin-top: 25px;
            display: grid;
            gap: 10px;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 13px;
            padding: 12px;
            border: 1px solid var(--line);
            border-radius: 10px;
            background: rgba(255,255,255,0.018);
            transition: 0.25s;
        }

        .contact-item:hover {
            border-color: rgba(179,0,0,0.4);
            transform: translateX(4px);
        }

        .contact-icon {
            width: 42px;
            height: 42px;
            min-width: 42px;
            border-radius: 10px;
            display: grid;
            place-items: center;
            color: #ff4242;
            background: var(--accent-soft);
        }

        .contact-icon svg {
            width: 20px;
            height: 20px;
            stroke: currentColor;
            fill: none;
            stroke-width: 1.8;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .contact-label {
            color: #777c87;
            display: block;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .contact-value {
            color: #e4e5e8;
            font-size: 12px;
            word-break: break-word;
        }

        .social-row {
            display: flex;
            flex-wrap: wrap;
            gap: 9px;
            margin-top: 18px;
        }

        .social-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 13px;
            border: 1px solid var(--line);
            border-radius: 8px;
            color: #d6d8dd;
            font-size: 11px;
            font-weight: 700;
            transition: 0.25s;
        }

        .social-btn:hover {
            border-color: var(--accent);
            color: white;
            transform: translateY(-2px);
        }

        .social-btn svg {
            width: 15px;
            height: 15px;
            fill: currentColor;
        }

        /* =========================
           FOOTER
        ========================= */

        footer {
            border-top: 1px solid var(--line);
            padding: 28px 0;
            color: #70747e;
            font-size: 11px;
        }

        .footer-inner {
            display: flex;
            justify-content: space-between;
            gap: 20px;
        }

        .back-top {
            color: #aaaeb7;
            transition: 0.2s;
        }

        .back-top:hover {
            color: var(--accent-light);
        }

        /* =========================
           REVEAL ANIMATION
        ========================= */

        .reveal {
            opacity: 0;
            transform: translateY(25px);
            transition: opacity 0.7s ease, transform 0.7s ease;
        }

        .reveal.show {
            opacity: 1;
            transform: translateY(0);
        }

        /* =========================
           RESPONSIVE
        ========================= */

        @media (max-width: 950px) {
            .hero-grid,
            .contact-grid {
                grid-template-columns: 1fr;
            }

            .hero-grid {
                text-align: center;
                gap: 50px;
            }

            .hero-description {
                margin-left: auto;
                margin-right: auto;
            }

            .hero-buttons {
                justify-content: center;
            }

            .hero-photo-wrap {
                order: -1;
            }

            .projects-grid {
                grid-template-columns: 1fr 1fr;
            }
        }

        @media (max-width: 760px) {
            .nav-links {
                display: none;
                position: absolute;
                top: 76px;
                left: 0;
                width: 100%;
                padding: 20px 6%;
                background: rgba(8,9,12,0.98);
                border-bottom: 1px solid var(--line);
                flex-direction: column;
                gap: 5px;
            }

            .nav-links.open {
                display: flex;
            }

            .nav-links a {
                padding: 12px 0;
            }

            .menu-btn {
                display: block;
            }

            .about-grid,
            .skills-grid,
            .projects-grid {
                grid-template-columns: 1fr;
            }

            .hero h1 {
                letter-spacing: -2px;
            }

            .info-row {
                grid-template-columns: 1fr;
                gap: 4px;
            }

            .footer-inner {
                flex-direction: column;
                text-align: center;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            html {
                scroll-behavior: auto;
            }

            .shape,
            .hero-photo-ring {
                animation: none !important;
            }

            .reveal {
                opacity: 1;
                transform: none;
            }
        }
    </style>
</head>

<body>

    <!-- Animated geometric background -->
    <div class="geometry" aria-hidden="true">
        <span class="shape one"></span>
        <span class="shape two"></span>
        <span class="shape three"></span>
        <span class="shape four"></span>
        <span class="shape five"></span>
    </div>

    <!-- Navigation -->
    <header class="navbar">
        <div class="container nav-inner">
            <a href="#home" class="brand">RHEA <span>DUMAGAT</span></a>

            <button class="menu-btn" id="menuBtn" aria-label="Open navigation">
                ☰
            </button>

            <nav class="nav-links" id="navLinks">
                <a href="#home" class="active">Home</a>
                <a href="#about">About</a>
                <a href="#family">Family</a>
                <a href="#education">Education</a>
                <a href="#skills">Skills</a>
                <a href="#projects">Projects</a>
                <a href="#certificates">Certificates</a>
                <a href="#contact">Contact</a>
            </nav>
        </div>
    </header>

    <!-- Hero -->
    <main>
        <section class="hero" id="home">
            <div class="container hero-grid">

                <div class="reveal">
                    <div class="eyebrow">
                        <span class="eyebrow-dot"></span>
                        DIGITAL PORTFOLIO
                    </div>

                    <h1>
                        RHEA
                        <span>DUMAGAT</span>
                    </h1>

                    <div class="hero-subtitle">
                        College Student &amp; Aspiring IT Professional
                    </div>

                    <p class="hero-description">
                        Welcome to my professional portfolio. I am a college
                        student interested in technology, programming, web
                        development, problem solving, and creative digital design.
                    </p>

                    <div class="hero-buttons">
                        <a href="#projects" class="btn btn-primary">
                            View My Projects →
                        </a>

                        <a href="#contact" class="btn btn-outline">
                            Contact Me
                        </a>
                    </div>
                </div>

                <div class="hero-photo-wrap reveal">
                    <div class="hero-photo-ring">
                        <div class="hero-photo">
                            <img src="/static/images/rhea.jpg"
                                 alt="Rhea Dumagat">
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <!-- About -->
        <section id="about">
            <div class="container">

                <div class="section-heading reveal">
                    <div class="section-kicker">01 — About Me</div>
                    <h2>Personal Information</h2>
                    <p>
                        A simple introduction to who I am and where I am currently based.
                    </p>
                </div>

                <div class="about-grid">

                    <div class="card reveal">
                        <div class="card-title">
                            <div class="title-icon">
                                <svg viewBox="0 0 24 24">
                                    <circle cx="12" cy="8" r="4"></circle>
                                    <path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"></path>
                                </svg>
                            </div>
                            About Me
                        </div>

                        <div class="info-list">
                            <div class="info-row">
                                <span class="info-label">Full Name</span>
                                <span class="info-value">Rhea Dumagat</span>
                            </div>

                            <div class="info-row">
                                <span class="info-label">Status</span>
                                <span class="info-value">College Student</span>
                            </div>

                            <div class="info-row">
                                <span class="info-label">Current Address</span>
                                <span class="info-value">P-3 Pualas, Don Carlos, Bukidnon</span>
                            </div>
                        </div>
                    </div>

                    <div class="card reveal">
                        <div class="card-title">
                            <div class="title-icon">
                                <svg viewBox="0 0 24 24">
                                    <path d="M20 21a8 8 0 0 0-16 0"></path>
                                    <circle cx="12" cy="7" r="4"></circle>
                                </svg>
                            </div>
                            Personal Statement
                        </div>

                        <p style="color:var(--muted); font-size:13px; line-height:1.9;">
                            I am continuously developing my knowledge and practical
                            skills in information technology. I enjoy learning
                            programming concepts, creating digital projects, solving
                            problems, and improving my ability to design useful and
                            user-friendly applications.
                        </p>
                    </div>

                </div>
            </div>
        </section>

        <!-- Family -->
        <section id="family">
            <div class="container">

                <div class="section-heading reveal">
                    <div class="section-kicker">02 — Family</div>
                    <h2>Family Background</h2>
                    <p>
                        The people who are an important part of my personal journey.
                    </p>
                </div>

                <div class="card family-card reveal">
                    <div class="info-list">

                        <div class="info-row">
                            <span class="info-label">Mother</span>
                            <span class="info-value">Annalisa L. Dumagat</span>
                        </div>

                        <div class="info-row">
                            <span class="info-label">Father</span>
                            <span class="info-value">N/A</span>
                        </div>

                        <div class="info-row">
                            <span class="info-label">Siblings</span>
                            <span class="info-value">
                                <div class="siblings">
                                    <span class="tag">Alkris Dumagat</span>
                                    <span class="tag">Mea Ann D. Castro</span>
                                    <span class="tag">Nathally D. Castro</span>
                                    <span class="tag">Mary Angel D. Castro</span>
                                    <span class="tag">Freya D. Castro</span>
                                </div>
                            </span>
                        </div>

                    </div>
                </div>

            </div>
        </section>

        <!-- Education -->
        <section id="education">
            <div class="container">

                <div class="section-heading reveal">
                    <div class="section-kicker">03 — Education</div>
                    <h2>My Educational Journey</h2>
                    <p>
                        My academic background from elementary school through college.
                    </p>
                </div>

                <div class="timeline">

                    <div class="timeline-item reveal">
                        <span class="timeline-dot"></span>
                        <div class="timeline-card">
                            <div class="timeline-level">Elementary</div>
                            <h3>Mahawan Elementary School</h3>
                            <p>Primary education</p>
                        </div>
                    </div>

                    <div class="timeline-item reveal">
                        <span class="timeline-dot"></span>
                        <div class="timeline-card">
                            <div class="timeline-level">Junior High School</div>
                            <h3>Old Nongnongan National High School</h3>
                            <p>Junior high school education</p>
                        </div>
                    </div>

                    <div class="timeline-item reveal">
                        <span class="timeline-dot"></span>
                        <div class="timeline-card">
                            <div class="timeline-level">Senior High School</div>
                            <h3>Loyola School Of Don Carlos, Inc.</h3>
                            <p>Senior high school education</p>
                        </div>
                    </div>

                    <div class="timeline-item reveal">
                        <span class="timeline-dot"></span>
                        <div class="timeline-card">
                            <div class="timeline-level">College</div>
                            <h3>Torres Capitol College</h3>
                            <p>Current college education</p>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Skills -->
        <section id="skills">
            <div class="container">

                <div class="section-heading reveal">
                    <div class="section-kicker">04 — Skills</div>
                    <h2>Technical &amp; Personal Skills</h2>
                    <p>
                        Skills that I am developing through academic work and personal projects.
                    </p>
                </div>

                <div class="skills-grid">

                    <div class="skill-card reveal">
                        <div class="skill-top">
                            <span class="skill-name">Python Programming</span>
                            <span class="skill-percent">85%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-width="85%"></div></div>
                        <div class="skill-note">Programming fundamentals and application development</div>
                    </div>

                    <div class="skill-card reveal">
                        <div class="skill-top">
                            <span class="skill-name">Java Programming</span>
                            <span class="skill-percent">75%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-width="75%"></div></div>
                        <div class="skill-note">Object-oriented programming and console applications</div>
                    </div>

                    <div class="skill-card reveal">
                        <div class="skill-top">
                            <span class="skill-name">HTML &amp; CSS</span>
                            <span class="skill-percent">85%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-width="85%"></div></div>
                        <div class="skill-note">Responsive website structure and styling</div>
                    </div>

                    <div class="skill-card reveal">
                        <div class="skill-top">
                            <span class="skill-name">UI Design</span>
                            <span class="skill-percent">80%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-width="80%"></div></div>
                        <div class="skill-note">Clean interfaces using Tkinter and web technologies</div>
                    </div>

                    <div class="skill-card reveal">
                        <div class="skill-top">
                            <span class="skill-name">Problem Solving</span>
                            <span class="skill-percent">90%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-width="90%"></div></div>
                        <div class="skill-note">Breaking problems into practical and logical steps</div>
                    </div>

                    <div class="skill-card reveal">
                        <div class="skill-top">
                            <span class="skill-name">Critical Thinking</span>
                            <span class="skill-percent">88%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-width="88%"></div></div>
                        <div class="skill-note">Analysis, decision-making, and solution evaluation</div>
                    </div>

                    <div class="skill-card reveal">
                        <div class="skill-top">
                            <span class="skill-name">Web Design</span>
                            <span class="skill-percent">80%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-width="80%"></div></div>
                        <div class="skill-note">Modern layouts, navigation, cards, and responsive design</div>
                    </div>

                    <div class="skill-card reveal">
                        <div class="skill-top">
                            <span class="skill-name">Communication</span>
                            <span class="skill-percent">85%</span>
                        </div>
                        <div class="skill-bar"><div class="skill-fill" data-width="85%"></div></div>
                        <div class="skill-note">Presenting ideas and working effectively with others</div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Projects -->
        <section id="projects">
            <div class="container">

                <div class="section-heading reveal">
                    <div class="section-kicker">05 — Projects</div>
                    <h2>Featured Projects</h2>
                    <p>
                        Academic and personal projects that demonstrate my interest in programming and technology.
                    </p>
                </div>

                <div class="projects-grid">

                    <article class="project-card reveal">
                        <div>
                            <div class="project-number">PROJECT 01</div>
                            <h3>Student Portal</h3>
                            <p>
                                A student management application for student accounts,
                                grades, schedules, and academic information.
                            </p>

                            <div class="project-tech">
                                <span class="tech">Python</span>
                                <span class="tech">Tkinter</span>
                                <span class="tech">JSON</span>
                            </div>
                        </div>

                        <a href="#contact" class="btn btn-outline">Discuss Project →</a>
                    </article>

                    <article class="project-card reveal">
                        <div>
                            <div class="project-number">PROJECT 02</div>
                            <h3>Grade Calculator</h3>
                            <p>
                                A Java program that calculates academic grades using
                                Prelim, Midterm, Semifinal, and Final grades.
                            </p>

                            <div class="project-tech">
                                <span class="tech">Java</span>
                                <span class="tech">Scanner</span>
                                <span class="tech">Logic</span>
                            </div>
                        </div>

                        <a href="#contact" class="btn btn-outline">Discuss Project →</a>
                    </article>

                    <article class="project-card reveal">
                        <div>
                            <div class="project-number">PROJECT 03</div>
                            <h3>BSIT Department Grading System</h3>
                            <p>
                                A Java desktop application built with Swing that calculates
                                term grades from attendance, assignments, quizzes, and exams,
                                and calculates the GWA from Prelim, Midterm, Semifinal, and
                                Final grades. It displays grade equivalents and pass/fail remarks.
                            </p>

                            <div class="project-tech">
                                <span class="tech">Java</span>
                                <span class="tech">Java Swing</span>
                                <span class="tech">AWT</span>
                                <span class="tech">Grade Calculation</span>
                            </div>
                        </div>

                        <a href="/grading-system" class="btn btn-primary">Open Grading System ↗</a>
                    </article>

                    <article class="project-card reveal">
                        <div>
                            <div class="project-number">PROJECT 04</div>
                            <h3>Digital Portfolio</h3>
                            <p>
                                A responsive portfolio website designed to present
                                personal information, education, skills, and projects.
                            </p>

                            <div class="project-tech">
                                <span class="tech">Python</span>
                                <span class="tech">Flask</span>
                                <span class="tech">HTML</span>
                                <span class="tech">CSS</span>
                            </div>
                        </div>

                        <a href="#home" class="btn btn-outline">View Portfolio →</a>
                    </article>

                    <article class="project-card reveal"
                             onclick="window.location.href='/open-studybuddy'"
                             onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();window.location.href='/open-studybuddy'}"
                             role="link" tabindex="0" aria-label="Open StudyBuddy project" style="cursor:pointer">
                        <div>
                            <div class="project-number">PROJECT 05</div>
                            <h3>StudyBuddy: Voice-Based Study Assistant</h3>
                            <p>
                                A study assistance web application that helps BSIT students
                                upload reviewers, generate practice questions, answer by voice
                                or text, review flashcards, and monitor study progress.
                            </p>

                            <div class="project-tech">
                                <span class="tech">Python</span>
                                <span class="tech">Flask</span>
                                <span class="tech">SQLite</span>
                                <span class="tech">AI / NLP</span>
                                <span class="tech">Speech API</span>
                            </div>
                        </div>

                        <a href="/open-studybuddy" class="btn btn-primary">Open StudyBuddy ↗</a>
                    </article>

                </div>
            </div>
        </section>

        <!-- Certificates -->
        <section id="certificates">
            <div class="container">
                <div class="section-heading reveal">
                    <div class="section-kicker">06 — Certificates</div>
                    <h2>Seminar Certificates</h2>
                    <p>
                        Certificates of participation in seminars and learning activities
                        related to my course and professional development.
                    </p>
                </div>

                <div class="projects-grid">
                    <article class="project-card certificate-card reveal">
                        <div>
                            <div class="project-number">CERTIFICATE 01</div>
                            <h3>Certificate of Participation 1</h3>
                            <p>
                                Proof of participation in a seminar or learning activity
                                related to Information Technology.
                            </p>
                            <a class="certificate-preview-link"
                               href="{{ url_for('static', filename='certificates/certificate1.jpg') }}"
                               target="_blank" rel="noopener noreferrer"
                               aria-label="Open Certificate 1 in a new tab">
                                <img class="certificate-preview"
                                     src="{{ url_for('static', filename='certificates/certificate1.jpg') }}"
                                     alt="Certificate of participation 1"
                                     loading="lazy">
                            </a>
                        </div>
                        <a class="btn btn-outline"
                           href="{{ url_for('static', filename='certificates/certificate1.jpg') }}"
                           target="_blank" rel="noopener noreferrer">View Certificate →</a>
                    </article>

                    <article class="project-card certificate-card reveal">
                        <div>
                            <div class="project-number">CERTIFICATE 02</div>
                            <h3>Certificate of Participation 2</h3>
                            <p>
                                Proof of participation in another seminar or learning activity
                                connected to my course and skills development.
                            </p>
                            <a class="certificate-preview-link"
                               href="{{ url_for('static', filename='certificates/certificate2.jpg') }}"
                               target="_blank" rel="noopener noreferrer"
                               aria-label="Open Certificate 2 in a new tab">
                                <img class="certificate-preview"
                                     src="{{ url_for('static', filename='certificates/certificate2.jpg') }}"
                                     alt="Certificate of participation 2"
                                     loading="lazy">
                            </a>
                        </div>
                        <a class="btn btn-outline"
                           href="{{ url_for('static', filename='certificates/certificate2.jpg') }}"
                           target="_blank" rel="noopener noreferrer">View Certificate →</a>
                    </article>
                </div>
            </div>
        </section>

        <!-- Contact -->
        <section id="contact">
            <div class="container">

                <div class="section-heading reveal">
                    <div class="section-kicker">07 — Contact</div>
                    <h2>Let's Connect</h2>
                    <p>
                        For school projects, collaboration, or professional inquiries,
                        you can reach me through the information below.
                    </p>
                </div>

                <div class="contact-grid">

                    <div class="contact-intro reveal">
                        <h3>Get in touch.</h3>
                        <p>
                            I am always interested in learning, building new projects,
                            and connecting with people who share an interest in
                            technology and creativity.
                        </p>

                        <div class="social-row">
                            <a class="social-btn" href="mailto:dumagatrhea199@gmail.com">
                                <svg viewBox="0 0 24 24">
                                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                                    <polyline points="22,6 12,13 2,6"/>
                                </svg>
                                Email
                            </a>

                            <a class="social-btn" href="tel:09262129782">
                                <svg viewBox="0 0 24 24">
                                    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.2 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.8 12.8 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.8 12.8 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                                </svg>
                                Call
                            </a>
                        </div>
                    </div>

                    <div class="card reveal">
                        <div class="contact-list">

                            <div class="contact-item">
                                <div class="contact-icon">
                                    <svg viewBox="0 0 24 24">
                                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.2 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.8 12.8 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.8 12.8 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                                    </svg>
                                </div>
                                <div>
                                    <span class="contact-label">Cellular Number</span>
                                    <span class="contact-value">09262129782</span>
                                </div>
                            </div>

                            <div class="contact-item">
                                <div class="contact-icon">
                                    <svg viewBox="0 0 24 24">
                                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                                        <polyline points="22,6 12,13 2,6"/>
                                    </svg>
                                </div>
                                <div>
                                    <span class="contact-label">Email Address</span>
                                    <span class="contact-value">dumagatrhea199@gmail.com</span>
                                </div>
                            </div>

                            <div class="contact-item">
                                <div class="contact-icon">
                                    <svg viewBox="0 0 24 24">
                                        <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
                                    </svg>
                                </div>
                                <div>
                                    <span class="contact-label">Facebook</span>
                                    <span class="contact-value">Rhea Dumagat</span>
                                </div>
                            </div>

                            <div class="contact-item">
                                <div class="contact-icon">
                                    <svg viewBox="0 0 24 24">
                                        <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
                                        <path d="M16 11.37a4 4 0 1 1-3.37-3.37A4 4 0 0 1 16 11.37z"/>
                                        <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>
                                    </svg>
                                </div>
                                <div>
                                    <span class="contact-label">Instagram</span>
                                    <span class="contact-value">rubygem.</span>
                                </div>
                            </div>

                        </div>
                    </div>

                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container footer-inner">
            <span>© 2026 Rhea Dumagat. All rights reserved.</span>
            <a href="#home" class="back-top">Back to top ↑</a>
        </div>
    </footer>

    <script>
        // Mobile navigation
        const menuBtn = document.getElementById("menuBtn");
        const navLinks = document.getElementById("navLinks");

        menuBtn.addEventListener("click", () => {
            navLinks.classList.toggle("open");
        });

        document.querySelectorAll(".nav-links a").forEach(link => {
            link.addEventListener("click", () => {
                navLinks.classList.remove("open");
            });
        });

        // Reveal elements as the user scrolls
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("show");
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12 });

        document.querySelectorAll(".reveal").forEach(el => {
            revealObserver.observe(el);
        });

        // Animate skill bars when they become visible
        const skillObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.querySelectorAll(".skill-fill").forEach(fill => {
                        fill.style.width = fill.dataset.width;
                    });
                    skillObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });

        document.querySelectorAll(".skills-grid").forEach(el => {
            skillObserver.observe(el);
        });

        // Highlight the current navigation section
        const sections = document.querySelectorAll("main section[id]");
        const links = document.querySelectorAll(".nav-links a");

        const activeObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    links.forEach(link => link.classList.remove("active"));
                    const active = document.querySelector(
                        '.nav-links a[href="#' + entry.target.id + '"]'
                    );
                    if (active) active.classList.add("active");
                }
            });
        }, {
            rootMargin: "-35% 0px -55% 0px"
        });

        sections.forEach(section => activeObserver.observe(section));
    </script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


GRADING_SYSTEM_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BSIT Department Grading System</title>
  <style>
    :root{--bg:#08090c;--panel:#15171d;--panel2:#101217;--text:#f5f5f5;--muted:#a8adb8;--line:rgba(255,255,255,.11);--red:#b30000;--red2:#e00000;--green:#38b879}
    *{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 80% 0%,rgba(179,0,0,.16),transparent 34%),var(--bg);font-family:Inter,Arial,sans-serif;color:var(--text);line-height:1.6}
    a{color:inherit;text-decoration:none}.wrap{width:min(960px,92%);margin:0 auto;padding:30px 0 60px}.top{display:flex;justify-content:space-between;align-items:center;gap:15px;margin-bottom:28px}.back,.btn{display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--line);border-radius:10px;padding:10px 15px;font-weight:700;cursor:pointer;color:var(--text);background:transparent}.btn-primary{background:var(--red);border-color:var(--red)}.btn-primary:hover{background:var(--red2)}
    .eyebrow{color:#ff7777;text-transform:uppercase;letter-spacing:2px;font-size:.76rem;font-weight:800}.hero h1{font-size:clamp(2rem,5vw,3.2rem);line-height:1.12;margin:8px 0 12px}.muted{color:var(--muted)}.notice{border:1px solid rgba(255,190,90,.3);background:rgba(255,190,90,.07);color:#f3d9a7;padding:12px 14px;border-radius:12px;font-size:.9rem;margin:22px 0}
    .panel{background:rgba(21,23,29,.94);border:1px solid var(--line);border-radius:18px;padding:clamp(18px,4vw,28px);margin:20px 0;box-shadow:0 20px 50px rgba(0,0,0,.2)}.panel h2{margin:0 0 5px;font-size:1.35rem}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.field label{display:block;color:#d8dbe2;font-weight:650;margin-bottom:7px}.field input{width:100%;padding:12px 13px;background:#0c0e12;border:1px solid #333742;border-radius:10px;color:var(--text);font:inherit;outline:none}.field input:focus{border-color:#e00000;box-shadow:0 0 0 3px rgba(224,0,0,.12)}.field small{display:block;color:var(--muted);margin-top:5px}.actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}.results{display:none}.results.show{display:block}.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:18px}.stat{padding:17px;background:var(--panel2);border:1px solid var(--line);border-radius:13px}.stat span{display:block;color:var(--muted);font-size:.85rem}.stat strong{display:block;font-size:1.65rem;margin-top:3px}.status{font-weight:800}.status.pass{color:var(--green)}.status.fail{color:#ff7777}.result-table{width:100%;border-collapse:collapse;margin-top:18px}.result-table th,.result-table td{text-align:left;padding:11px 8px;border-bottom:1px solid var(--line)}.result-table th{color:var(--muted);font-size:.86rem}.foot{color:var(--muted);font-size:.85rem;margin-top:28px;text-align:center}
    @media(max-width:650px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:1fr}.top{align-items:flex-start;flex-direction:column}.result-table th,.result-table td{font-size:.9rem}}
  </style>
</head>
<body>
  <main class="wrap">
    <div class="top"><a class="back" href="/">← Back to Portfolio</a><span class="eyebrow">Interactive Project Demo</span></div>
    <header class="hero"><div class="eyebrow">Project 03 · Academic Utility</div><h1>BSIT Department<br>Grading System</h1><p class="muted">Enter sample scores to calculate a term grade, then enter the four term grades to calculate the General Weighted Average (GWA).</p></header>
    <div class="notice"><strong>Original Java formulas:</strong> Term Grade = Attendance + Assignment + Quiz + Exam, rounded using the original <code>Math.round(total * 101.0) / 101.0</code> expression. GWA = (Prelim + Midterm + Semifinal + Final) / 4, rounded to two decimal places. Grade-equivalent ranges are copied from the original Calculate button logic.</div>
    <section class="panel">
      <h2>1. Calculate Term Grade</h2><p class="muted">Enter scores from 0 to 100.</p>
      <form id="termForm">
        <div class="grid">
          <div class="field"><label for="studentName">Student name (optional)</label><input id="studentName" type="text" placeholder="Enter student name" maxlength="80"></div>
          <div class="field"><label for="subjectName">Subject (optional)</label><input id="subjectName" type="text" placeholder="Enter subject" maxlength="80"></div>
          <div class="field"><label for="attendance">Attendance</label><input id="attendance" type="number" min="0" max="100" step="0.01" required placeholder="Enter attendance score"><small>Enter the value used in your original program.</small></div>
          <div class="field"><label for="assignment">Assignment</label><input id="assignment" type="number" min="0" max="100" step="0.01" required placeholder="Enter assignment score"></div>
          <div class="field"><label for="quiz">Quiz</label><input id="quiz" type="number" min="0" max="100" step="0.01" required placeholder="Enter quiz score"></div>
          <div class="field"><label for="exam">Exam</label><input id="exam" type="number" min="0" max="100" step="0.01" required placeholder="Enter exam score"></div>
        </div>
        <div class="actions"><button class="btn btn-primary" type="submit">Calculate Term Grade</button><button class="btn" type="reset" id="resetTerm">Clear Scores</button></div>
      </form>
      <div id="termResults" class="results" aria-live="polite"><div class="stats"><div class="stat"><span>Computed term grade</span><strong id="termGrade">—</strong></div><div class="stat"><span>Grade equivalent</span><strong id="termEquivalent">—</strong></div><div class="stat"><span>Remarks</span><strong id="termRemark" class="status">—</strong></div></div><p id="termSummary" class="muted"></p></div>
    </section>
    <section class="panel">
      <h2>2. Calculate General Weighted Average</h2><p class="muted">Enter the calculated grade for each grading period.</p>
      <form id="gwaForm"><div class="grid">
        <div class="field"><label for="prelim">Prelim grade</label><input id="prelim" type="number" min="0" max="100" step="0.01" required placeholder="0–100"></div>
        <div class="field"><label for="midterm">Midterm grade</label><input id="midterm" type="number" min="0" max="100" step="0.01" required placeholder="0–100"></div>
        <div class="field"><label for="semifinal">Semifinal grade</label><input id="semifinal" type="number" min="0" max="100" step="0.01" required placeholder="0–100"></div>
        <div class="field"><label for="finalGrade">Final grade</label><input id="finalGrade" type="number" min="0" max="100" step="0.01" required placeholder="0–100"></div>
      </div><div class="actions"><button class="btn btn-primary" type="submit">Calculate GWA</button><button class="btn" type="reset">Clear Grades</button><button class="btn" type="button" id="useTermGrade">Use term grade above</button></div></form>
      <div id="gwaResults" class="results" aria-live="polite"><div class="stats"><div class="stat"><span>GWA / average</span><strong id="gwaValue">—</strong></div><div class="stat"><span>Grade equivalent</span><strong id="gwaEquivalent">—</strong></div><div class="stat"><span>Remarks</span><strong id="gwaRemark" class="status">—</strong></div></div><table class="result-table"><thead><tr><th>Grading period</th><th>Grade</th><th>Equivalent</th></tr></thead><tbody id="gwaRows"></tbody></table></div>
    </section>
    <p class="foot">BSIT Department Grading System · Portfolio demonstration · No grades are stored or sent to a server.</p>
  </main>
  <script>
    const $ = id => document.getElementById(id);
    // Grade bands below mirror the conditional ranges in the supplied Java source.
    function gradeEquivalent(score, mode){
      if ((mode === 'term' && score >= 101) || (mode === 'gwa' && score >= 100)) return 'Invalid grade';
      if (score >= 98.5 && (mode === 'term' ? score < 101 : score < 100)) return '1.00';
      else if (score >= 95.5 && score <= 98.4) return '1.25';
      else if (score >= 92.5 && score <= 95.4) return '1.5';
      else if (score >= 89.5 && score <= 92.4) return '1.75';
      else if (score >= 86.5 && score <= 89.4) return '2.0';
      else if (score >= 83.5 && score <= 86.4) return '2.25';
      else if (score >= 80.5 && score <= 83.4) return '2.5';
      else if (score >= 77.5 && score <= 80.4) return '2.75';
      else if (score >= 74.5 && score <= 77.4) return '3.0';
      else if (score <= 77.4) return '5.0';
      else return 'Invalid grade';
    }
    function setRemarkFromEquivalent(element, equivalent){
      // Matches the original Java action listeners, including their Invalid grade branch.
      const remarks = equivalent === 'Invalid grade' ? 'Passed' : (Number(equivalent) <= 3.0 ? 'Passed' : 'Failed');
      element.textContent = remarks;
      element.className = 'status ' + (remarks === 'Passed' ? 'pass' : 'fail');
    }
    function validateForm(form){
      for(const input of form.querySelectorAll('input[type="number"]')){
        const value=Number(input.value);
        if(input.value.trim()==='' || !Number.isFinite(value) || value<0 || value>100){input.focus(); alert('Please enter a score from 0 to 100 for every required grade field.'); return false;}
      } return true;
    }
    function setRemark(element, score){element.textContent=score>=75?'PASSED':'FAILED';element.className='status '+(score>=75?'pass':'fail');}
    let latestTermGrade=null;
    $('termForm').addEventListener('submit',e=>{
      e.preventDefault(); if(!validateForm(e.currentTarget)) return;
      const attendance=Number($('attendance').value), assignment=Number($('assignment').value), quiz=Number($('quiz').value), exam=Number($('exam').value);
      // The Java Term Grade action adds the four values and uses Math.round(total * 101.0) / 101.0.
      const total=attendance+assignment+quiz+exam;
      const result=Math.round(total*101.0)/101.0;
      latestTermGrade=result;
      const equivalent=gradeEquivalent(result,'term');
      $('termGrade').textContent=String(result); $('termEquivalent').textContent=equivalent; setRemarkFromEquivalent($('termRemark'),equivalent);
      const name=$('studentName').value.trim(), subject=$('subjectName').value.trim();
      $('termSummary').textContent=(name?'Student: '+name+'. ':'')+(subject?'Subject: '+subject+'. ':'')+'Original formula: ('+attendance+' + '+assignment+' + '+quiz+' + '+exam+') = '+total+'; rounded as Math.round(total × 101.0) / 101.0.';
      $('termResults').classList.add('show');
    });
    $('resetTerm').addEventListener('click',()=>{setTimeout(()=>{$('termResults').classList.remove('show');latestTermGrade=null;},0)});
    $('gwaForm').addEventListener('submit',e=>{
      e.preventDefault(); if(!validateForm(e.currentTarget)) return;
      const terms=[['Prelim',Number($('prelim').value)],['Midterm',Number($('midterm').value)],['Semifinal',Number($('semifinal').value)],['Final',Number($('finalGrade').value)]];
      const total=terms.reduce((sum,item)=>sum+item[1],0);
      const average=Math.round((total/4)*100.0)/100.0;
      const equivalent=gradeEquivalent(average,'gwa');
      $('gwaValue').textContent=average.toFixed(2); $('gwaEquivalent').textContent=equivalent; setRemarkFromEquivalent($('gwaRemark'),equivalent);
      $('gwaRows').innerHTML=terms.map(([label,value])=>'<tr><td>'+label+'</td><td>'+value.toFixed(2)+'</td><td>'+gradeEquivalent(value,'gwa')+'</td></tr>').join('');
      $('gwaResults').classList.add('show');
    });
    $('useTermGrade').addEventListener('click',()=>{
      if(latestTermGrade===null){alert('Calculate a term grade first.');return;}
      const empty=['prelim','midterm','semifinal','finalGrade'].find(id=>$(id).value==='');
      if(empty){$(empty).value=latestTermGrade.toFixed(2);$(empty).focus();}else{alert('All four grading-period fields already have values. Clear a field first if you want to insert the term grade.');}
    });
  </script>
</body>
</html>
"""


@app.route("/grading-system")
def grading_system():
    return render_template_string(GRADING_SYSTEM_HTML)


@app.route("/open-studybuddy")
def open_studybuddy():
    return redirect(STUDYBUDDY_URL)


if __name__ == "__main__":
    print("=" * 55)
    print("       RHEA DUMAGAT — PROFESSIONAL PORTFOLIO")
    print("=" * 55)
    print("Website: http://127.0.0.1:5000")
    print("Photo:   static/images/rhea.jpg")
    print("Press CTRL+C to stop the server.")
    print("=" * 55)

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )

