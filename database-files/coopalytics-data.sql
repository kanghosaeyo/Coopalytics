-- Applications table (60 rows - with realistic GPA and skill matching)
INSERT INTO applications (applicationId, dateTimeApplied, status, resume, gpa, coverLetter, coopPositionId) VALUES
-- Applications that match student majors, GPAs, and skills
-- Charlie Stout (CS major, GPA 3.7, has Python, Java, JavaScript, React, etc.)
(1, '2025-01-15 10:30:00', 'Submitted', 'Resume content for Charlie Stout...', 3.7, 'Cover letter expressing interest in software development...', 1), -- Software Developer (req GPA 3.0, skill 1-Python) ✓
(2, '2025-01-16 14:20:00', 'Under Review', 'Resume content for Charlie Stout...', 3.7, 'Cover letter for full stack developer...', 16), -- Full Stack Developer (req GPA 3.2, skill 3-JavaScript) ✓

-- Liam Williams (Business major, GPA 3.5, has Excel, PowerPoint, Project Management, etc.)
(3, '2025-01-18 09:45:00', 'Submitted', 'Resume content for Liam Williams...', 3.5, 'Cover letter highlighting business experience...', 5), -- Financial Analyst (req GPA 3.4, skill 13-Excel) ✓
(4, '2025-01-20 16:15:00', 'Draft', 'Resume content for Liam Williams...', 3.5, NULL, 10), -- Business Analyst (req GPA 3.0, skill 15-Project Management) ✓

-- Sophia Brown (Engineering major, GPA 3.8, has C++, Excel, Project Management, etc.)
(5, '2025-01-22 11:30:00', 'Submitted', 'Resume content for Sophia Brown...', 3.8, 'Cover letter for engineering role...', 18), -- Robotics Engineer (req GPA 3.4, skill 21-C++) ✓
(6, '2025-01-25 08:45:00', 'Under Review', 'Resume content for Sophia Brown...', 3.8, 'Manufacturing engineering application...', 43), -- Manufacturing Engineer (req GPA 3.3, skill 15-Project Management) ✓

-- Noah Davis (Data Science major, GPA 3.9, has Python, ML, Data Analysis, etc.)
(7, '2025-01-28 13:20:00', 'Submitted', 'Resume content for Noah Davis...', 3.9, 'Machine learning interest cover letter...', 11), -- ML Intern (req GPA 3.6, skill 11-ML) ✓
(8, '2025-01-30 10:00:00', 'Rejected', 'Resume content for Noah Davis...', 3.9, 'Data engineering application...', 29), -- Data Engineer (req GPA 3.4, skill 1-Python) ✓

-- Olivia Miller (Marketing major, GPA 3.4, has Excel, PowerPoint, Communication, etc.)
(9, '2025-02-01 15:30:00', 'Draft', 'Resume content for Olivia Miller...', 3.4, NULL, 3), -- Marketing Assistant (req GPA 2.8, skill 17-Communication) ✓
(10, '2025-02-03 12:45:00', 'Submitted', 'Resume content for Olivia Miller...', 3.4, 'Digital marketing interest...', 19), -- Digital Marketing (req GPA 2.7, skill 17-Communication) ✓

-- Mason Wilson (Cybersecurity major, GPA 3.6, has Python, SQL, AWS, etc.)
(11, '2025-02-05 09:15:00', 'Under Review', 'Resume content for Mason Wilson...', 3.6, 'Cybersecurity application...', 4), -- Cybersecurity Intern (req GPA 3.3, skill 6-SQL) ✓
(12, '2025-02-07 14:00:00', 'Submitted', 'Resume content for Mason Wilson...', 3.6, 'Security analyst interest...', 32), -- Security Analyst (req GPA 3.2, skill 6-SQL) ✓

-- Ava Moore (Biomedical Eng major, GPA 3.7, has Python, Data Analysis, etc.)
(13, '2025-02-08 11:20:00', 'Draft', 'Resume content for Ava Moore...', 3.7, NULL, 7), -- Biotech Research (req GPA 3.5, skill 12-Data Analysis) ✓
(14, '2025-02-10 16:45:00', 'Submitted', 'Resume content for Ava Moore...', 3.7, 'Healthcare data analysis...', 15), -- Healthcare Data Analyst (req GPA 3.3, skill 12-Data Analysis) ✓

-- Ethan Taylor (Finance major, GPA 3.8, has Excel, Data Analysis, etc.)
(15, '2025-02-12 08:30:00', 'Under Review', 'Resume content for Ethan Taylor...', 3.8, 'Finance analyst application...', 27), -- Finance Intern (req GPA 3.3, skill 13-Excel) ✓
(16, '2025-02-14 13:15:00', 'Submitted', 'Resume content for Ethan Taylor...', 3.8, 'Business intelligence focus...', 23), -- Business Intelligence (req GPA 3.2, skill 37-Tableau) ✓

-- Isabella Anderson (Psychology major, GPA 3.3, has Excel, PowerPoint, Communication, etc.)
(17, '2025-02-16 10:45:00', 'Draft', 'Resume content for Isabella Anderson...', 3.3, NULL, 42), -- HR Analytics (req GPA 2.9, skill 12-Data Analysis) ✓
(18, '2025-02-18 15:20:00', 'Submitted', 'Resume content for Isabella Anderson...', 3.3, 'Customer success passion...', 46), -- Customer Success (req GPA 2.8, skill 17-Communication) ✓

-- James Thomas (Mechanical Eng major, GPA 3.5, has C++, C#, Excel, etc.)
(19, '2025-02-20 12:00:00', 'Under Review', 'Resume content for James Thomas...', 3.5, 'Automation engineering interest...', 45), -- Automation Engineer (req GPA 3.4, skill 1-Python) ✓
(20, '2025-02-22 09:30:00', 'Submitted', 'Resume content for James Thomas...', 3.5, 'Manufacturing focus...', 43), -- Manufacturing Engineer (req GPA 3.3, skill 15-Project Management) ✓

-- Continue with remaining students (matching majors, GPAs, and skills)

-- Mia Jackson (CS major, GPA 3.9, has Python, Java, JavaScript, React, Node.js, etc.)
(21, '2025-01-17 14:30:00', 'Submitted', 'Resume content for Mia Jackson...', 3.9, 'Full stack development application...', 16), -- Full Stack Developer (req GPA 3.2, skill 3-JavaScript) ✓
(22, '2025-01-19 11:15:00', 'Under Review', 'Resume content for Mia Jackson...', 3.9, 'Backend development interest...', 22), -- Backend Developer (req GPA 3.0, skill 2-Java) ✓

-- Lucas White (Business with Data Science minor, GPA 3.4, has Excel, PowerPoint, Project Management, Python)
(23, '2025-01-21 16:00:00', 'Draft', 'Resume content for Lucas White...', 3.4, NULL, 10), -- Business Analyst (req GPA 3.0, skill 15-Project Management) ✓
(24, '2025-01-23 13:45:00', 'Submitted', 'Resume content for Lucas White...', 3.4, 'Operations analysis application...', 33), -- Operations Analyst (req GPA 3.0, skill 13-Excel) ✓

-- Charlotte Harris (Environmental Eng major, GPA 3.6, has Python, Data Analysis, Excel, etc.)
(25, '2025-01-26 10:20:00', 'Under Review', 'Resume content for Charlotte Harris...', 3.6, 'Environmental engineering focus...', 8), -- Environmental Engineer (req GPA 3.1, skill 15-Project Management) ✓
(26, '2025-01-29 15:10:00', 'Submitted', 'Resume content for Charlotte Harris...', 3.6, 'Infrastructure interest...', 49), -- Infrastructure Engineer (req GPA 3.2, skill 8-AWS) ✓

-- Benjamin Martin (Information Systems major, GPA 3.7, has Python, SQL, AWS, Excel, etc.)
(27, '2025-02-02 08:50:00', 'Draft', 'Resume content for Benjamin Martin...', 3.7, NULL, 26), -- Systems Administrator (req GPA 3.0, skill 8-AWS) ✓
(28, '2025-02-04 12:30:00', 'Submitted', 'Resume content for Benjamin Martin...', 3.7, 'Database administration...', 35), -- Database Administrator (req GPA 3.3, skill 6-SQL) ✓

-- Amelia Garcia (Chemical Eng major, GPA 3.5, has Python, Data Analysis, Excel, etc.)
(29, '2025-02-06 14:40:00', 'Under Review', 'Resume content for Amelia Garcia...', 3.5, 'Chemical engineering application...', 43), -- Manufacturing Engineer (req GPA 3.3, skill 15-Project Management) ✓
(30, '2025-02-09 11:55:00', 'Submitted', 'Resume content for Amelia Garcia...', 3.5, 'Research assistant focus...', 25), -- Research Assistant (req GPA 3.4, skill 12-Data Analysis) ✓

-- Henry Rodriguez (CS with Math minor, GPA 3.2, has Python, Java, JavaScript, C++)
(31, '2025-02-11 16:25:00', 'Draft', 'Resume content for Henry Rodriguez...', 3.2, NULL, 1), -- Software Developer (req GPA 3.0, skill 1-Python) ✓
(32, '2025-01-24 09:40:00', 'Submitted', 'Resume content for Henry Rodriguez...', 3.2, 'Web development interest...', 31), -- Web Developer (req GPA 3.0, skill 30-HTML) ✓

-- Harper Lewis (Design with Art minor, GPA 3.8, has Adobe Creative, UI/UX Design, etc.)
(33, '2025-01-27 14:55:00', 'Under Review', 'Resume content for Harper Lewis...', 3.8, 'UX design passion letter...', 6), -- UX Design Intern (req GPA 3.0, skill 40-UI/UX Design) ✓
(34, '2025-01-31 10:35:00', 'Submitted', 'Resume content for Harper Lewis...', 3.8, 'Product design interest...', 48), -- Product Design Intern (req GPA 3.0, skill 40-UI/UX Design) ✓

-- Alexander Lee (Electrical Eng major, GPA 3.6, has C++, C#, Excel, etc.)
(35, '2025-02-13 13:20:00', 'Draft', 'Resume content for Alexander Lee...', 3.6, NULL, 18), -- Robotics Engineer (req GPA 3.4, skill 21-C++) ✓
(36, '2025-02-15 08:15:00', 'Submitted', 'Resume content for Alexander Lee...', 3.6, 'Automation engineering...', 45), -- Automation Engineer (req GPA 3.4, skill 1-Python) ✓

-- Evelyn Walker (International Business with Spanish minor, GPA 3.4, has Excel, PowerPoint, Communication, etc.)
(37, '2025-02-17 15:45:00', 'Under Review', 'Resume content for Evelyn Walker...', 3.4, 'International business focus...', 50), -- Business Development (req GPA 2.9, skill 17-Communication) ✓
(38, '2025-02-19 12:10:00', 'Submitted', 'Resume content for Evelyn Walker...', 3.4, 'Project coordination...', 30), -- Project Coordinator (req GPA 2.8, skill 15-Project Management) ✓

-- Sebastian Hall (Data Science major, GPA 3.8, has Python, ML, Data Analysis, Tableau, etc.)
(39, '2025-02-21 09:25:00', 'Draft', 'Resume content for Sebastian Hall...', 3.8, NULL, 11), -- ML Intern (req GPA 3.6, skill 11-ML) ✓
(40, '2025-01-14 16:30:00', 'Submitted', 'Resume content for Sebastian Hall...', 3.8, 'Computer vision interest...', 47), -- Computer Vision Co-op (req GPA 3.5, skill 11-ML) ✓

-- Aria Allen (Marketing major, GPA 3.3, has Excel, PowerPoint, Communication, etc.)
(41, '2025-01-16 11:45:00', 'Under Review', 'Resume content for Aria Allen...', 3.3, 'Marketing coordination interest...', 19), -- Digital Marketing (req GPA 2.7, skill 17-Communication) ✓
(42, '2025-01-18 14:20:00', 'Submitted', 'Resume content for Aria Allen...', 3.3, 'Sales analytics application...', 36), -- Sales Analytics (req GPA 2.9, skill 12-Data Analysis) ✓

-- Owen Young (CS major, GPA 3.1, has Python, Java, JavaScript, Git)
(43, '2025-01-20 10:05:00', 'Draft', 'Resume content for Owen Young...', 3.1, NULL, 1), -- Software Developer (req GPA 3.0, skill 1-Python) ✓
(44, '2025-01-22 15:35:00', 'Submitted', 'Resume content for Owen Young...', 3.1, 'Web development passion...', 31), -- Web Developer (req GPA 3.0, skill 30-HTML) ✓

-- Luna King (Business with Finance minor, GPA 3.7, has Excel, PowerPoint, Project Management, etc.)
(45, '2025-01-25 12:50:00', 'Under Review', 'Resume content for Luna King...', 3.7, 'Financial analysis...', 5), -- Financial Analyst (req GPA 3.4, skill 13-Excel) ✓
(46, '2025-01-28 08:40:00', 'Submitted', 'Resume content for Luna King...', 3.7, 'Business intelligence focus...', 23), -- Business Intelligence (req GPA 3.2, skill 37-Tableau) ✓

-- Grayson Wright (Cybersecurity major, GPA 3.5, has Python, SQL, AWS, Docker, etc.)
(47, '2025-01-30 13:25:00', 'Draft', 'Resume content for Grayson Wright...', 3.5, NULL, 4), -- Cybersecurity Intern (req GPA 3.3, skill 6-SQL) ✓
(48, '2025-02-01 16:15:00', 'Submitted', 'Resume content for Grayson Wright...', 3.5, 'Network engineering interest...', 41), -- Network Engineer (req GPA 3.1, skill 8-AWS) ✓

-- Chloe Lopez (Bioengineering major, GPA 3.6, has Python, Data Analysis, etc.)
(49, '2025-02-03 11:00:00', 'Under Review', 'Resume content for Chloe Lopez...', 3.6, 'Bioengineering research passion...', 7), -- Biotech Research (req GPA 3.5, skill 12-Data Analysis) ✓
(50, '2025-02-05 14:45:00', 'Submitted', 'Resume content for Chloe Lopez...', 3.6, 'Healthcare data focus...', 15), -- Healthcare Data Analyst (req GPA 3.3, skill 12-Data Analysis) ✓

-- Carter Hill (Information Systems with Business minor, GPA 3.4, has Python, SQL, Excel, Project Management)
(51, '2025-02-07 09:30:00', 'Draft', 'Resume content for Carter Hill...', 3.4, NULL, 26), -- Systems Administrator (req GPA 3.0, skill 8-AWS) ✓
(52, '2025-02-10 12:15:00', 'Submitted', 'Resume content for Carter Hill...', 3.4, 'Business analysis application...', 10), -- Business Analyst (req GPA 3.0, skill 15-Project Management) ✓

-- Zoey Scott (Environmental Eng major, GPA 3.7, has Python, Data Analysis, Excel, Project Management)
(53, '2025-02-12 15:50:00', 'Under Review', 'Resume content for Zoey Scott...', 3.7, 'Environmental focus...', 8), -- Environmental Engineer (req GPA 3.1, skill 15-Project Management) ✓
(54, '2025-02-14 10:25:00', 'Submitted', 'Resume content for Zoey Scott...', 3.7, 'Cloud engineering passion...', 20), -- Cloud Engineer (req GPA 3.5, skill 8-AWS) ✓

-- Luke Green (Mechanical Eng major, GPA 3.3, has C++, C#, Excel, Project Management)
(55, '2025-02-16 13:40:00', 'Draft', 'Resume content for Luke Green...', 3.3, NULL, 18), -- Robotics Engineer (req GPA 3.4, skill 21-C++) ❌ GPA too low
(56, '2025-02-18 08:55:00', 'Submitted', 'Resume content for Luke Green...', 3.3, 'Manufacturing engineering...', 43), -- Manufacturing Engineer (req GPA 3.3, skill 15-Project Management) ✓

-- Lily Adams (Design major, GPA 3.9, has Adobe Creative, UI/UX Design, Excel, PowerPoint)
(57, '2025-02-20 14:10:00', 'Under Review', 'Resume content for Lily Adams...', 3.9, 'Product design interest...', 48), -- Product Design Intern (req GPA 3.0, skill 40-UI/UX Design) ✓
(58, '2025-02-22 11:35:00', 'Submitted', 'Resume content for Lily Adams...', 3.9, 'Technical writing passion...', 38), -- Technical Writer (req GPA 2.8, skill 17-Communication) ✓

-- Jack Baker (CS major, GPA 3.5, has Python, Java, JavaScript, React, Git)
(59, '2025-01-13 16:20:00', 'Draft', 'Resume content for Jack Baker...', 3.5, NULL, 16), -- Full Stack Developer (req GPA 3.2, skill 3-JavaScript) ✓
(60, '2025-01-15 12:45:00', 'Submitted', 'Resume content for Jack Baker...', 3.5, 'Backend development interest...', 22); -- Backend Developer (req GPA 3.0, skill 2-Java) ✓-- Sample data for coopalytics database
USE `coopalytics`;

-- Skills table (40 rows - strong entity)
INSERT INTO skills (skillId, name, category) VALUES
(1, 'Python', 'Programming'),
(2, 'Java', 'Programming'),
(3, 'JavaScript', 'Programming'),
(4, 'React', 'Web Development'),
(5, 'Node.js', 'Web Development'),
(6, 'SQL', 'Database'),
(7, 'MongoDB', 'Database'),
(8, 'AWS', 'Cloud'),
(9, 'Docker', 'DevOps'),
(10, 'Git', 'Version Control'),
(11, 'Machine Learning', 'Data Science'),
(12, 'Data Analysis', 'Data Science'),
(13, 'Excel', 'Office'),
(14, 'PowerPoint', 'Office'),
(15, 'Project Management', 'Management'),
(16, 'Agile', 'Management'),
(17, 'Communication', 'Soft Skills'),
(18, 'Leadership', 'Soft Skills'),
(19, 'Problem Solving', 'Soft Skills'),
(20, 'Teamwork', 'Soft Skills'),
(21, 'C++', 'Programming'),
(22, 'C#', 'Programming'),
(23, 'PHP', 'Programming'),
(24, 'Ruby', 'Programming'),
(25, 'Swift', 'Programming'),
(26, 'Kotlin', 'Programming'),
(27, 'Angular', 'Web Development'),
(28, 'Vue.js', 'Web Development'),
(29, 'CSS', 'Web Development'),
(30, 'HTML', 'Web Development'),
(31, 'PostgreSQL', 'Database'),
(32, 'MySQL', 'Database'),
(33, 'Azure', 'Cloud'),
(34, 'GCP', 'Cloud'),
(35, 'Kubernetes', 'DevOps'),
(36, 'Jenkins', 'DevOps'),
(37, 'Tableau', 'Data Science'),
(38, 'R', 'Data Science'),
(39, 'Adobe Creative', 'Design'),
(40, 'UI/UX Design', 'Design');

-- Company Profiles table (35 rows - strong entity)
INSERT INTO companyProfiles (companyProfileId, name, bio, industry, websiteLink) VALUES
(1, 'TechNova Inc', 'Leading software development company specializing in enterprise solutions and cloud infrastructure.', 'Technology', 'www.technova.com'),
(2, 'DataFlow Systems', 'Data analytics and business intelligence platform provider serving Fortune 500 companies.', 'Technology', 'www.dataflow.com'),
(3, 'GreenEnergy Corp', 'Renewable energy solutions and sustainable technology development company.', 'Energy', 'www.greenenergy.com'),
(4, 'HealthTech Solutions', 'Healthcare technology company developing innovative medical software and devices.', 'Healthcare', 'www.healthtech.com'),
(5, 'FinanceFirst Bank', 'Regional bank offering comprehensive financial services and digital banking solutions.', 'Finance', 'www.financefirst.com'),
(6, 'AutoInnovate Ltd', 'Automotive technology company focused on electric vehicles and autonomous driving.', 'Automotive', 'www.autoinnovate.com'),
(7, 'CloudSecure Pro', 'Cybersecurity firm specializing in cloud security and data protection services.', 'Technology', 'www.cloudsecure.com'),
(8, 'BioResearch Labs', 'Biotechnology research company developing pharmaceutical and medical innovations.', 'Healthcare', 'www.bioresearch.com'),
(9, 'EcoDesign Studio', 'Sustainable architecture and environmental design consultancy.', 'Construction', 'www.ecodesign.com'),
(10, 'LogiFlow Corp', 'Supply chain management and logistics optimization company.', 'Logistics', 'www.logiflow.com'),
(11, 'MediaCraft Agency', 'Digital marketing and content creation agency for modern brands.', 'Marketing', 'www.mediacraft.com'),
(12, 'RoboTech Systems', 'Industrial automation and robotics solutions provider.', 'Manufacturing', 'www.robotech.com'),
(13, 'EduTech Platform', 'Educational technology company creating online learning solutions.', 'Education', 'www.edutech.com'),
(14, 'SportsTech Inc', 'Sports analytics and performance technology company.', 'Sports', 'www.sportstech.com'),
(15, 'FoodChain Solutions', 'Food supply chain technology and sustainability solutions.', 'Food', 'www.foodchain.com'),
(16, 'RetailNext Corp', 'Retail technology and e-commerce platform solutions.', 'Retail', 'www.retailnext.com'),
(17, 'GameDev Studios', 'Independent game development studio creating mobile and PC games.', 'Gaming', 'www.gamedev.com'),
(18, 'AeroSpace Dynamics', 'Aerospace engineering and satellite technology company.', 'Aerospace', 'www.aerospace.com'),
(19, 'CryptoSecure Ltd', 'Blockchain technology and cryptocurrency security solutions.', 'Finance', 'www.cryptosecure.com'),
(20, 'AIVision Tech', 'Computer vision and artificial intelligence solutions provider.', 'Technology', 'www.aivision.com'),
(21, 'CleanWater Corp', 'Water treatment and environmental remediation technology.', 'Environment', 'www.cleanwater.com'),
(22, 'SmartHome Systems', 'Internet of Things and smart home automation solutions.', 'Technology', 'www.smarthome.com'),
(23, 'ConsultPro Group', 'Management consulting firm specializing in digital transformation.', 'Consulting', 'www.consultpro.com'),
(24, 'MedDevice Innovations', 'Medical device manufacturing and healthcare equipment.', 'Healthcare', 'www.meddevice.com'),
(25, 'SolarPower Solutions', 'Solar energy installation and renewable power systems.', 'Energy', 'www.solarpower.com'),
(26, 'TravelTech App', 'Travel technology platform and booking solutions.', 'Travel', 'www.traveltech.com'),
(27, 'FashionForward LLC', 'Sustainable fashion technology and supply chain solutions.', 'Fashion', 'www.fashionforward.com'),
(28, 'InsureTech Pro', 'Insurance technology and risk assessment solutions.', 'Insurance', 'www.insuretech.com'),
(29, 'AgriTech Farms', 'Agricultural technology and precision farming solutions.', 'Agriculture', 'www.agritech.com'),
(30, 'VirtualReality Lab', 'Virtual and augmented reality development company.', 'Technology', 'www.vrlab.com'),
(31, 'PetCare Tech', 'Pet health monitoring and veterinary technology solutions.', 'Healthcare', 'www.petcare.com'),
(32, 'MusicStream Pro', 'Music streaming platform and audio technology company.', 'Entertainment', 'www.musicstream.com'),
(33, 'LegalTech Firm', 'Legal technology and case management software provider.', 'Legal', 'www.legaltech.com'),
(34, 'DroneLogistics Co', 'Drone delivery and aerial logistics solutions.', 'Logistics', 'www.dronelogistics.com'),
(35, 'WellnessTech Hub', 'Mental health and wellness technology platform.', 'Healthcare', 'www.wellnesstech.com');

-- Users table (48 rows - strong entity, mix of students, advisors, employers, and admins)
INSERT INTO users (userId, firstName, lastName, email, phone, major, minor, college, gradYear, grade, companyProfileId, industry) VALUES
-- Students (userId 1-30)
(1, 'Charlie', 'Stout', 'c.stout@student.edu', '555-0101', 'Computer Science', 'Mathematics', 'NEU', '2026', 'Junior', NULL, NULL),
(2, 'Liam', 'Williams', 'l.williams@student.edu', '555-0102', 'Business', 'Economics', 'NEU', '2025', 'Senior', NULL, NULL),
(3, 'Sophia', 'Brown', 's.brown@student.edu', '555-0103', 'Engineering', 'Physics', 'NEU', '2027', 'Sophomore', NULL, NULL),
(4, 'Noah', 'Davis', 'n.davis@student.edu', '555-0104', 'Data Science', NULL, 'NEU', '2026', 'Junior', NULL, NULL),
(5, 'Olivia', 'Miller', 'o.miller@student.edu', '555-0105', 'Marketing', 'Psychology', 'NEU', '2025', 'Senior', NULL, NULL),
(6, 'Mason', 'Wilson', 'm.wilson@student.edu', '555-0106', 'Cybersecurity', NULL, 'NEU', '2026', 'Junior', NULL, NULL),
(7, 'Ava', 'Moore', 'a.moore@student.edu', '555-0107', 'Biomedical Eng', 'Chemistry', 'NEU', '2027', 'Sophomore', NULL, NULL),
(8, 'Ethan', 'Taylor', 'e.taylor@student.edu', '555-0108', 'Finance', NULL, 'NEU', '2025', 'Senior', NULL, NULL),
(9, 'Isabella', 'Anderson', 'i.anderson@student.edu', '555-0109', 'Psychology', 'Sociology', 'NEU', '2026', 'Junior', NULL, NULL),
(10, 'James', 'Thomas', 'j.thomas@student.edu', '555-0110', 'Mechanical Eng', NULL, 'NEU', '2027', 'Sophomore', NULL, NULL),
(11, 'Mia', 'Jackson', 'm.jackson@student.edu', '555-0111', 'Computer Science', NULL, 'NEU', '2025', 'Senior', NULL, NULL),
(12, 'Lucas', 'White', 'l.white@student.edu', '555-0112', 'Business', 'Data Science', 'NEU', '2026', 'Junior', NULL, NULL),
(13, 'Charlotte', 'Harris', 'c.harris@student.edu', '555-0113', 'Environmental Eng', 'Biology', 'NEU', '2027', 'Sophomore', NULL, NULL),
(14, 'Benjamin', 'Martin', 'b.martin@student.edu', '555-0114', 'Information Systems', NULL, 'NEU', '2025', 'Senior', NULL, NULL),
(15, 'Amelia', 'Garcia', 'a.garcia@student.edu', '555-0115', 'Chemical Eng', NULL, 'NEU', '2026', 'Junior', NULL, NULL),
(16, 'Henry', 'Rodriguez', 'h.rodriguez@student.edu', '555-0116', 'Computer Science', 'Mathematics', 'NEU', '2027', 'Sophomore', NULL, NULL),
(17, 'Harper', 'Lewis', 'h.lewis@student.edu', '555-0117', 'Design', 'Art', 'NEU', '2025', 'Senior', NULL, NULL),
(18, 'Alexander', 'Lee', 'a.lee@student.edu', '555-0118', 'Electrical Eng', NULL, 'NEU', '2026', 'Junior', NULL, NULL),
(19, 'Evelyn', 'Walker', 'e.walker@student.edu', '555-0119', 'International Business', 'Spanish', 'NEU', '2027', 'Sophomore', NULL, NULL),
(20, 'Sebastian', 'Hall', 's.hall@student.edu', '555-0120', 'Data Science', NULL, 'NEU', '2025', 'Senior', NULL, NULL),
(21, 'Aria', 'Allen', 'a.allen@student.edu', '555-0121', 'Marketing', NULL, 'NEU', '2026', 'Junior', NULL, NULL),
(22, 'Owen', 'Young', 'o.young@student.edu', '555-0122', 'Computer Science', NULL, 'NEU', '2027', 'Sophomore', NULL, NULL),
(23, 'Luna', 'King', 'l.king@student.edu', '555-0123', 'Business', 'Finance', 'NEU', '2025', 'Senior', NULL, NULL),
(24, 'Grayson', 'Wright', 'g.wright@student.edu', '555-0124', 'Cybersecurity', NULL, 'NEU', '2026', 'Junior', NULL, NULL),
(25, 'Chloe', 'Lopez', 'c.lopez@student.edu', '555-0125', 'Bioengineering', NULL, 'NEU', '2027', 'Sophomore', NULL, NULL),
(26, 'Carter', 'Hill', 'c.hill@student.edu', '555-0126', 'Information Systems', 'Business', 'NEU', '2025', 'Senior', NULL, NULL),
(27, 'Zoey', 'Scott', 'z.scott@student.edu', '555-0127', 'Environmental Eng', NULL, 'NEU', '2026', 'Junior', NULL, NULL),
(28, 'Luke', 'Green', 'l.green@student.edu', '555-0128', 'Mechanical Eng', NULL, 'NEU', '2027', 'Sophomore', NULL, NULL),
(29, 'Lily', 'Adams', 'l.adams@student.edu', '555-0129', 'Design', NULL, 'NEU', '2025', 'Senior', NULL, NULL),
(30, 'Jack', 'Baker', 'j.baker@student.edu', '555-0130', 'Computer Science', NULL, 'NEU', '2026', 'Junior', NULL, NULL),
-- Advisors (userId 31-36)
(31, 'Sarah', 'Martinez', 's.martinez@neu.edu', '555-0301', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Academic'),
(32, 'Michael', 'Chen', 'm.chen@neu.edu', '555-0302', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Academic'),
(33, 'Jennifer', 'Kim', 'j.kim@neu.edu', '555-0303', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Academic'),
(34, 'David', 'Johnson', 'd.johnson@neu.edu', '555-0304', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Academic'),
(35, 'Lisa', 'Thompson', 'l.thompson@neu.edu', '555-0305', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Academic'),
(36, 'Robert', 'Wilson', 'r.wilson@neu.edu', '555-0306', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Academic'),
-- Employers (userId 37-44)
(37, 'Phoebe', 'Hwang', 'p.hwang@technova.com', '555-0401', NULL, NULL, NULL, NULL, NULL, 1, 'Technology'),
(38, 'Marcus', 'Roberts', 'm.roberts@dataflow.com', '555-0402', NULL, NULL, NULL, NULL, NULL, 2, 'Technology'),
(39, 'Elena', 'Thompson', 'e.thompson@greenenergy.com', '555-0403', NULL, NULL, NULL, NULL, NULL, 3, 'Energy'),
(40, 'James', 'Martinez', 'j.martinez@healthtech.com', '555-0404', NULL, NULL, NULL, NULL, NULL, 4, 'Healthcare'),
(41, 'Rachel', 'Anderson', 'r.anderson@financefirst.com', '555-0405', NULL, NULL, NULL, NULL, NULL, 5, 'Finance'),
(42, 'Daniel', 'Clark', 'd.clark@autoinnovate.com', '555-0406', NULL, NULL, NULL, NULL, NULL, 6, 'Automotive'),
(43, 'Amanda', 'Lewis', 'a.lewis@cloudsecure.com', '555-0407', NULL, NULL, NULL, NULL, NULL, 7, 'Technology'),
(44, 'Christopher', 'Walker', 'c.walker@bioresearch.com', '555-0408', NULL, NULL, NULL, NULL, NULL, 8, 'Healthcare'),
-- Admins (userId 45-48)
(45, 'Kaelyn', 'Dunn', 'k.dunn@neu.edu', '555-0501', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Administration'),
(46, 'Tyler', 'Rodriguez', 't.rodriguez@neu.edu', '555-0502', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Administration'),
(47, 'Madison', 'Foster', 'm.foster@neu.edu', '555-0503', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Administration'),
(48, 'Jordan', 'Bell', 'j.bell@neu.edu', '555-0504', NULL, NULL, 'NEU', NULL, NULL, NULL, 'Administration');

-- Demographics table (48 rows - for ALL users)
INSERT INTO demographics (demographicId, gender, race, nationality, sexuality, disability) VALUES
-- Students (1-30)
(1, 'Male', 'White', 'American', 'Heterosexual', NULL),
(2, 'Male', 'Hispanic', 'American', 'Heterosexual', NULL),
(3, 'Female', 'Asian', 'American', 'Heterosexual', NULL),
(4, 'Male', 'Black', 'American', 'Heterosexual', NULL),
(5, 'Female', 'White', 'American', 'Bisexual', NULL),
(6, 'Male', 'White', 'American', 'Heterosexual', 'ADHD'),
(7, 'Female', 'Mixed Race', 'American', 'Heterosexual', NULL),
(8, 'Male', 'Asian', 'International', 'Heterosexual', NULL),
(9, 'Female', 'Hispanic', 'American', 'Heterosexual', 'Anxiety'),
(10, 'Male', 'White', 'American', 'Gay', NULL),
(11, 'Female', 'Black', 'American', 'Lesbian', NULL),
(12, 'Male', 'White', 'American', 'Heterosexual', NULL),
(13, 'Female', 'Native American', 'American', 'Heterosexual', NULL),
(14, 'Male', 'Asian', 'American', 'Heterosexual', 'Dyslexia'),
(15, 'Female', 'White', 'International', 'Heterosexual', NULL),
(16, 'Male', 'Hispanic', 'American', 'Bisexual', NULL),
(17, 'Female', 'Asian', 'American', 'Heterosexual', NULL),
(18, 'Male', 'Black', 'American', 'Heterosexual', NULL),
(19, 'Female', 'White', 'International', 'Heterosexual', NULL),
(20, 'Male', 'Mixed Race', 'American', 'Heterosexual', 'Depression'),
(21, 'Female', 'Hispanic', 'American', 'Heterosexual', NULL),
(22, 'Male', 'White', 'American', 'Heterosexual', NULL),
(23, 'Female', 'Asian', 'International', 'Heterosexual', NULL),
(24, 'Male', 'White', 'American', 'Gay', NULL),
(25, 'Female', 'Black', 'American', 'Heterosexual', NULL),
(26, 'Male', 'Hispanic', 'American', 'Heterosexual', 'Autism'),
(27, 'Female', 'White', 'American', 'Bisexual', NULL),
(28, 'Male', 'Asian', 'American', 'Heterosexual', NULL),
(29, 'Female', 'Mixed Race', 'American', 'Heterosexual', NULL),
(30, 'Male', 'White', 'American', 'Heterosexual', NULL),
-- Advisors (31-36)
(31, 'Female', 'Hispanic', 'American', 'Heterosexual', NULL),
(32, 'Male', 'Asian', 'American', 'Heterosexual', NULL),
(33, 'Female', 'Korean', 'American', 'Heterosexual', NULL),
(34, 'Male', 'White', 'American', 'Heterosexual', NULL),
(35, 'Female', 'Black', 'American', 'Heterosexual', NULL),
(36, 'Male', 'White', 'American', 'Gay', NULL),
-- Employers (37-44)
(37, 'Female', 'Asian', 'American', 'Heterosexual', NULL),
(38, 'Male', 'White', 'American', 'Heterosexual', NULL),
(39, 'Female', 'Hispanic', 'American', 'Bisexual', NULL),
(40, 'Male', 'Hispanic', 'American', 'Heterosexual', NULL),
(41, 'Female', 'Black', 'American', 'Heterosexual', NULL),
(42, 'Male', 'White', 'American', 'Heterosexual', NULL),
(43, 'Female', 'White', 'American', 'Lesbian', NULL),
(44, 'Male', 'Mixed Race', 'American', 'Heterosexual', NULL),
-- Admins (45-48)
(45, 'Female', 'White', 'American', 'Heterosexual', NULL),
(46, 'Male', 'Hispanic', 'American', 'Heterosexual', NULL),
(47, 'Female', 'Asian', 'American', 'Bisexual', NULL),
(48, 'Non-binary', 'Black', 'American', 'Pansexual', NULL);

-- Coop Positions table (50 rows - weak entity)
INSERT INTO coopPositions (coopPositionId, title, location, description, hourlyPay, requiredSkillsId, desiredSkillsId, desiredGPA, deadline, startDate, endDate, flag, industry) VALUES
(1, 'Software Developer Intern', 'Boston, MA', 'Develop web applications using modern frameworks and participate in agile development processes.', 22.50, 1, 4, 3.0, '2025-02-15 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(2, 'Data Analyst Co-op', 'Cambridge, MA', 'Analyze business data and create reports using SQL and Python for data-driven insights.', 20.00, 12, 11, 3.2, '2025-02-20 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(3, 'Marketing Assistant', 'New York, NY', 'Support digital marketing campaigns and social media strategy development.', 18.50, 17, 14, 2.8, '2025-03-01 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Marketing'),
(4, 'Cybersecurity Intern', 'Burlington, MA', 'Assist with security assessments and vulnerability testing in cloud environments.', 25.00, 6, 8, 3.3, '2025-02-10 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(5, 'Financial Analyst Co-op', 'Boston, MA', 'Support financial modeling and investment analysis for banking operations.', 21.00, 13, 12, 3.4, '2025-02-25 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Finance'),
(6, 'UX Design Intern', 'San Francisco, CA', 'Create user interface designs and conduct user research for mobile applications.', 24.00, 40, 39, 3.0, '2025-03-05 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(7, 'Biotech Research Co-op', 'Cambridge, MA', 'Conduct laboratory research and assist with clinical trial data analysis.', 19.50, 12, 11, 3.5, '2025-02-28 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Healthcare'),
(8, 'Environmental Engineer', 'Portland, OR', 'Work on renewable energy projects and sustainability assessments.', 23.00, 15, 12, 3.1, '2025-03-10 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Energy'),
(9, 'DevOps Intern', 'Seattle, WA', 'Manage CI/CD pipelines and cloud infrastructure using AWS and Docker.', 26.00, 9, 35, 3.2, '2025-02-12 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(10, 'Business Analyst Co-op', 'Chicago, IL', 'Analyze business processes and requirements for software implementation.', 20.50, 15, 13, 3.0, '2025-03-15 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Consulting'),
(11, 'Machine Learning Intern', 'Austin, TX', 'Develop ML models for predictive analytics and data processing pipelines.', 28.00, 11, 1, 3.6, '2025-02-18 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(12, 'Mobile App Developer', 'Los Angeles, CA', 'Build iOS and Android applications using native and cross-platform technologies.', 24.50, 25, 26, 3.1, '2025-03-20 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(13, 'Supply Chain Analyst', 'Atlanta, GA', 'Optimize logistics operations and analyze supply chain performance metrics.', 19.00, 12, 15, 2.9, '2025-02-22 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Logistics'),
(14, 'Game Developer Intern', 'San Diego, CA', 'Create game mechanics and features using Unity and C# programming.', 22.00, 22, 21, 3.0, '2025-03-25 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Gaming'),
(15, 'Healthcare Data Analyst', 'Philadelphia, PA', 'Analyze patient data and healthcare outcomes for medical research.', 21.50, 12, 37, 3.3, '2025-02-14 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Healthcare'),
(16, 'Full Stack Developer', 'Denver, CO', 'Build end-to-end web applications using React, Node.js, and databases.', 25.50, 3, 5, 3.2, '2025-03-08 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(17, 'Quality Assurance Co-op', 'Miami, FL', 'Test software applications and develop automated testing frameworks.', 18.00, 3, 10, 2.8, '2025-02-26 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(18, 'Robotics Engineer Intern', 'Detroit, MI', 'Design and program robotic systems for manufacturing automation.', 24.00, 21, 11, 3.4, '2025-03-12 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Manufacturing'),
(19, 'Digital Marketing Co-op', 'Nashville, TN', 'Manage social media campaigns and analyze digital marketing performance.', 17.50, 17, 12, 2.7, '2025-02-16 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Marketing'),
(20, 'Cloud Engineer Intern', 'Phoenix, AZ', 'Deploy and manage cloud infrastructure using AWS and Azure platforms.', 27.00, 8, 33, 3.5, '2025-03-18 23:59:59', '2025-06-01', '2025-12-01', FALSE, 'Technology'),
(21, 'Product Manager Co-op', 'San Jose, CA', 'Assist with product roadmap planning and coordinate development teams.', 23.50, 15, 17, 3.1, '2025-02-08 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Technology'),
(22, 'Backend Developer Intern', 'Portland, OR', 'Build server-side applications and APIs using Java and microservices.', 24.00, 2, 6, 3.0, '2025-02-24 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Technology'),
(23, 'Business Intelligence', 'Dallas, TX', 'Create dashboards and reports for executive decision making.', 20.50, 37, 13, 3.2, '2025-03-22 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Finance'),
(24, 'Frontend Developer Co-op', 'Tampa, FL', 'Develop user interfaces using React and modern CSS frameworks.', 22.00, 4, 29, 2.9, '2025-02-11 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Technology'),
(25, 'Research Assistant', 'Baltimore, MD', 'Support biomedical research projects and data collection efforts.', 16.50, 12, 38, 3.4, '2025-03-14 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Healthcare'),
(26, 'Systems Administrator', 'Salt Lake City, UT', 'Maintain IT infrastructure and provide technical support services.', 21.00, 8, 9, 3.0, '2025-02-19 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Technology'),
(27, 'Finance Intern', 'Minneapolis, MN', 'Assist with financial planning and budget analysis for corporate clients.', 19.00, 13, 12, 3.3, '2025-03-28 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Finance'),
(28, 'Software QA Engineer', 'Orlando, FL', 'Design test cases and automate testing procedures for software releases.', 20.00, 10, 3, 3.1, '2025-02-13 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Technology'),
(29, 'Data Engineer Co-op', 'Charlotte, NC', 'Build data pipelines and manage ETL processes for analytics platforms.', 25.00, 1, 7, 3.4, '2025-03-30 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Technology'),
(30, 'Project Coordinator', 'Kansas City, MO', 'Coordinate cross-functional teams and manage project timelines.', 18.00, 15, 16, 2.8, '2025-02-21 23:59:59', '2025-09-01', '2026-03-01', FALSE, 'Consulting'),
(31, 'Web Developer Intern', 'Las Vegas, NV', 'Create responsive websites and web applications for client projects.', 21.50, 30, 4, 3.0, '2025-03-06 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Technology'),
(32, 'Security Analyst Co-op', 'Raleigh, NC', 'Monitor security systems and investigate potential cyber threats.', 23.00, 6, 8, 3.2, '2025-02-17 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Technology'),
(33, 'Operations Analyst', 'Columbus, OH', 'Improve operational efficiency and analyze business performance metrics.', 19.50, 13, 15, 3.0, '2025-03-24 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Operations'),
(34, 'Android Developer', 'Indianapolis, IN', 'Develop native Android applications using Kotlin and Java.', 23.50, 26, 2, 3.1, '2025-02-09 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Technology'),
(35, 'Database Administrator', 'Memphis, TN', 'Manage database systems and optimize query performance.', 22.00, 6, 31, 3.3, '2025-03-16 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Technology'),
(36, 'Sales Analytics Intern', 'Louisville, KY', 'Analyze sales data and create performance reports for management.', 17.00, 12, 14, 2.9, '2025-02-23 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Sales'),
(37, 'IoT Developer Co-op', 'Oklahoma City, OK', 'Develop Internet of Things applications and sensor integration systems.', 24.50, 3, 1, 3.2, '2025-03-26 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Technology'),
(38, 'Technical Writer', 'Richmond, VA', 'Create technical documentation and user manuals for software products.', 18.50, 17, 14, 2.8, '2025-02-15 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Technology'),
(39, 'Blockchain Developer', 'Providence, RI', 'Build decentralized applications and smart contracts using blockchain technology.', 29.00, 3, 22, 3.5, '2025-03-11 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Finance'),
(40, 'AI Research Intern', 'Hartford, CT', 'Conduct artificial intelligence research and develop machine learning algorithms.', 26.50, 11, 1, 3.6, '2025-02-27 23:59:59', '2026-01-01', '2026-07-01', FALSE, 'Technology'),
(41, 'Network Engineer Co-op', 'Bridgeport, CT', 'Design and maintain network infrastructure and troubleshoot connectivity issues.', 21.50, 8, 32, 3.1, '2025-03-19 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Technology'),
(42, 'HR Analytics Intern', 'Newark, NJ', 'Analyze employee data and support human resources decision making.', 17.50, 12, 13, 2.9, '2025-02-12 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Human Resources'),
(43, 'Manufacturing Engineer', 'Buffalo, NY', 'Optimize production processes and implement lean manufacturing principles.', 22.50, 15, 12, 3.3, '2025-03-21 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Manufacturing'),
(44, 'Content Creator Co-op', 'Syracuse, NY', 'Develop multimedia content and manage brand social media presence.', 16.00, 39, 17, 2.7, '2025-02-20 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Marketing'),
(45, 'Automation Engineer', 'Rochester, NY', 'Design automated systems and implement robotic process automation.', 25.50, 1, 21, 3.4, '2025-03-13 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Manufacturing'),
(46, 'Customer Success Intern', 'Albany, NY', 'Support customer onboarding and analyze customer satisfaction metrics.', 17.00, 17, 12, 2.8, '2025-02-25 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Customer Service'),
(47, 'Computer Vision Co-op', 'Burlington, VT', 'Develop image processing algorithms and computer vision applications.', 27.50, 11, 1, 3.5, '2025-03-17 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Technology'),
(48, 'Product Design Intern', 'Manchester, NH', 'Create product prototypes and conduct user experience research.', 20.00, 40, 39, 3.0, '2025-02-14 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Design'),
(49, 'Infrastructure Engineer', 'Portland, ME', 'Manage cloud infrastructure and implement DevOps best practices.', 24.00, 8, 35, 3.2, '2025-03-23 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Technology'),
(50, 'Business Development', 'Concord, NH', 'Identify new business opportunities and support partnership development.', 18.50, 17, 15, 2.9, '2025-02-18 23:59:59', '2026-06-01', '2026-12-01', FALSE, 'Business');

-- Skill Details table (150 rows - bridge table for M:N relationship between students and skills)
INSERT INTO skillDetails (skillId, studentId, proficiencyLevel) VALUES
-- Student 1 (Emma Johnson) - Computer Science major
(1, 1, 4), (2, 1, 3), (3, 1, 5), (4, 1, 4), (5, 1, 3), (6, 1, 4), (10, 1, 5), (17, 1, 4), (19, 1, 4), (20, 1, 5),
-- Student 2 (Liam Williams) - Business major
(13, 2, 5), (14, 2, 4), (15, 2, 4), (16, 2, 3), (17, 2, 5), (18, 2, 4), (19, 2, 4), (20, 2, 5),
-- Student 3 (Sophia Brown) - Engineering major
(21, 3, 4), (13, 3, 3), (15, 3, 3), (17, 3, 4), (19, 3, 5), (20, 3, 4),
-- Student 4 (Noah Davis) - Data Science major
(1, 4, 5), (11, 4, 4), (12, 4, 5), (37, 4, 4), (38, 4, 3), (6, 4, 4), (17, 4, 4), (19, 4, 5), (20, 4, 4),
-- Student 5 (Olivia Miller) - Marketing major
(13, 5, 4), (14, 5, 5), (17, 5, 5), (18, 5, 3), (19, 5, 4), (20, 5, 5), (39, 5, 3),
-- Student 6 (Mason Wilson) - Cybersecurity major
(1, 6, 4), (6, 6, 5), (8, 6, 4), (9, 6, 3), (10, 6, 4), (17, 6, 4), (19, 6, 5), (20, 6, 4),
-- Student 7 (Ava Moore) - Biomedical Engineering major
(1, 7, 3), (12, 7, 4), (13, 7, 3), (17, 7, 4), (19, 7, 5), (20, 7, 4),
-- Student 8 (Ethan Taylor) - Finance major
(13, 8, 5), (14, 8, 4), (12, 8, 4), (17, 8, 4), (19, 8, 4), (20, 8, 4),
-- Student 9 (Isabella Anderson) - Psychology major
(13, 9, 4), (14, 9, 4), (17, 9, 5), (18, 9, 4), (19, 9, 5), (20, 9, 5),
-- Student 10 (James Thomas) - Mechanical Engineering major
(21, 10, 4), (22, 10, 3), (13, 10, 3), (15, 10, 4), (17, 10, 3), (19, 10, 4), (20, 10, 4),
-- Student 11 (Mia Jackson) - Computer Science major
(1, 11, 5), (2, 11, 4), (3, 11, 4), (4, 11, 5), (5, 11, 4), (6, 11, 3), (10, 11, 5), (17, 11, 4), (19, 11, 4), (20, 11, 5),
-- Student 12 (Lucas White) - Business major with Data Science minor
(13, 12, 4), (14, 12, 4), (15, 12, 4), (12, 12, 4), (1, 12, 3), (17, 12, 4), (19, 12, 4), (20, 12, 4),
-- Student 13 (Charlotte Harris) - Environmental Engineering major
(1, 13, 3), (12, 13, 3), (13, 13, 4), (15, 13, 4), (17, 13, 4), (19, 13, 5), (20, 13, 4),
-- Student 14 (Benjamin Martin) - Information Systems major
(1, 14, 4), (6, 14, 4), (8, 14, 3), (13, 14, 4), (15, 14, 4), (17, 14, 4), (19, 14, 4), (20, 14, 4),
-- Student 15 (Amelia Garcia) - Chemical Engineering major
(1, 15, 3), (12, 15, 4), (13, 15, 3), (15, 15, 3), (17, 15, 4), (19, 15, 4), (20, 15, 4),
-- Continue with remaining students...
(1, 16, 4), (2, 16, 3), (3, 16, 3), (21, 16, 4), (17, 16, 3), (19, 16, 4), (20, 16, 4),
(39, 17, 5), (40, 17, 5), (13, 17, 3), (14, 17, 4), (17, 17, 5), (19, 17, 4), (20, 17, 4),
(21, 18, 4), (22, 18, 3), (1, 18, 3), (13, 18, 3), (17, 18, 3), (19, 18, 4), (20, 18, 4),
(13, 19, 4), (14, 19, 4), (15, 19, 3), (17, 19, 5), (18, 19, 3), (19, 19, 4), (20, 19, 5),
(1, 20, 5), (11, 20, 5), (12, 20, 5), (37, 20, 4), (6, 20, 4), (17, 20, 4), (19, 20, 5), (20, 20, 4),
(13, 21, 4), (14, 21, 4), (17, 21, 5), (18, 21, 3), (19, 21, 4), (20, 21, 5),
(1, 22, 3), (2, 22, 3), (3, 22, 4), (10, 22, 4), (17, 22, 3), (19, 22, 4), (20, 22, 4),
(13, 23, 5), (14, 23, 4), (15, 23, 4), (17, 23, 4), (19, 23, 4), (20, 23, 4),
(1, 24, 4), (6, 24, 5), (8, 24, 4), (9, 24, 3), (17, 24, 4), (19, 24, 5), (20, 24, 4),
(1, 25, 3), (12, 25, 4), (17, 25, 4), (19, 25, 4), (20, 25, 4),
(1, 26, 4), (6, 26, 3), (13, 26, 4), (15, 26, 4), (17, 26, 4), (19, 26, 4), (20, 26, 4),
(1, 27, 3), (12, 27, 3), (13, 27, 3), (15, 27, 4), (17, 27, 4), (19, 27, 5), (20, 27, 4),
(21, 28, 4), (22, 28, 3), (13, 28, 3), (15, 28, 3), (17, 28, 3), (19, 28, 4), (20, 28, 4),
(39, 29, 5), (40, 29, 4), (13, 29, 3), (14, 29, 4), (17, 29, 5), (19, 29, 4), (20, 29, 4),
(1, 30, 4), (2, 30, 3), (3, 30, 4), (4, 30, 3), (10, 30, 4), (17, 30, 4), (19, 30, 4), (20, 30, 5);

-- Advisor-Advisee relationships (60 rows - bridge table)
INSERT INTO advisor_advisee (studentId, advisorId, flag) VALUES
(1, 31, FALSE), (1, 32, FALSE),
(2, 35, FALSE), (2, 36, FALSE),
(3, 33, FALSE), (3, 34, FALSE),
(4, 32, FALSE), (4, 31, FALSE),
(5, 35, FALSE), (5, 33, FALSE),
(6, 31, FALSE), (6, 34, FALSE),
(7, 34, FALSE), (7, 35, FALSE),
(8, 35, FALSE), (8, 36, FALSE),
(9, 33, FALSE), (9, 34, FALSE),
(10, 34, FALSE), (10, 36, FALSE),
(11, 31, FALSE), (11, 32, FALSE),
(12, 35, FALSE), (12, 36, FALSE),
(13, 33, FALSE), (13, 34, FALSE),
(14, 31, FALSE), (14, 32, FALSE),
(15, 33, FALSE), (15, 35, FALSE),
(16, 31, FALSE), (16, 32, FALSE),
(17, 33, FALSE), (17, 34, FALSE),
(18, 34, FALSE), (18, 31, FALSE),
(19, 35, FALSE), (19, 36, FALSE),
(20, 32, FALSE), (20, 31, FALSE),
(21, 35, FALSE), (21, 33, FALSE),
(22, 31, FALSE), (22, 32, FALSE),
(23, 35, FALSE), (23, 36, FALSE),
(24, 31, FALSE), (24, 34, FALSE),
(25, 34, FALSE), (25, 35, FALSE),
(26, 31, FALSE), (26, 32, FALSE),
(27, 33, FALSE), (27, 34, FALSE),
(28, 34, FALSE), (28, 36, FALSE),
(29, 33, FALSE), (29, 34, FALSE),
(30, 31, FALSE), (30, 32, FALSE); FALSE), (29, 34, FALSE),
(30, 31, FALSE), (30, 32, FALSE);

-- Worked At Position relationships (75 rows - bridge table for past co-ops with NO OVERLAPPING DATES)
INSERT INTO workedAtPos (studentId, coopPositionId, startDate, endDate, companyRating) VALUES
-- Past co-op experiences for senior students (chronological order, no overlaps)
-- Student 2 (Liam Williams) - Business major, Senior
(2, 30, '2022-01-01', '2022-06-01', 4), -- Project Coordinator (business-related)
(2, 23, '2023-01-01', '2023-06-01', 5), -- Business Intelligence 
(2, 10, '2024-01-01', '2024-06-01', 4), -- Business Analyst Co-op

-- Student 5 (Olivia Miller) - Marketing major, Senior  
(5, 36, '2022-06-01', '2022-12-01', 3), -- Sales Analytics (marketing-related)
(5, 19, '2023-06-01', '2023-12-01', 4), -- Digital Marketing Co-op
(5, 44, '2024-06-01', '2024-12-01', 3), -- Content Creator Co-op

-- Student 8 (Ethan Taylor) - Finance major, Senior
(8, 27, '2022-01-01', '2022-06-01', 4), -- Finance Intern
(8, 33, '2023-01-01', '2023-06-01', 4), -- Operations Analyst
(8, 23, '2024-01-01', '2024-06-01', 5), -- Business Intelligence

-- Student 11 (Mia Jackson) - Computer Science major, Senior
(11, 17, '2022-06-01', '2022-12-01', 3), -- Quality Assurance Co-op
(11, 22, '2023-06-01', '2023-12-01', 5), -- Backend Developer Intern
(11, 16, '2024-06-01', '2024-12-01', 4), -- Full Stack Developer

-- Student 12 (Lucas White) - Business with Data Science minor, Junior
(12, 30, '2023-01-01', '2023-06-01', 4), -- Project Coordinator
(12, 33, '2024-01-01', '2024-06-01', 3), -- Operations Analyst

-- Student 14 (Benjamin Martin) - Information Systems major, Senior
(14, 26, '2022-06-01', '2022-12-01', 4), -- Systems Administrator
(14, 35, '2023-06-01', '2023-12-01', 4), -- Database Administrator
(14, 28, '2024-06-01', '2024-12-01', 5), -- Software QA Engineer

-- Student 17 (Harper Lewis) - Design major, Senior
(17, 48, '2023-01-01', '2023-06-01', 5), -- Product Design Intern
(17, 44, '2024-01-01', '2024-06-01', 4), -- Content Creator Co-op

-- Student 20 (Sebastian Hall) - Data Science major, Senior
(20, 29, '2022-06-01', '2022-12-01', 5), -- Data Engineer Co-op
(20, 11, '2023-06-01', '2023-12-01', 5), -- Machine Learning Intern
(20, 47, '2024-06-01', '2024-12-01', 4), -- Computer Vision Co-op

-- Student 23 (Luna King) - Business with Finance minor, Senior
(23, 27, '2023-01-01', '2023-06-01', 3), -- Finance Intern
(23, 23, '2024-01-01', '2024-06-01', 4), -- Business Intelligence

-- Student 26 (Carter Hill) - Information Systems with Business minor, Senior
(26, 35, '2023-06-01', '2023-12-01', 4), -- Database Administrator
(26, 26, '2024-06-01', '2024-12-01', 4), -- Systems Administrator

-- Student 29 (Lily Adams) - Design major, Senior
(29, 48, '2023-06-01', '2023-12-01', 4), -- Product Design Intern
(29, 44, '2024-06-01', '2024-12-01', 5), -- Content Creator Co-op

-- Junior students with one co-op experience (appropriate to their majors/skills)
-- Student 1 (Charlie Stout) - Computer Science major
(1, 17, '2024-01-01', '2024-06-01', 4), -- Quality Assurance Co-op

-- Student 4 (Noah Davis) - Data Science major
(4, 29, '2024-01-01', '2024-06-01', 5), -- Data Engineer Co-op

-- Student 6 (Mason Wilson) - Cybersecurity major
(6, 32, '2024-01-01', '2024-06-01', 4), -- Security Analyst Co-op

-- Student 9 (Isabella Anderson) - Psychology major
(9, 42, '2024-01-01', '2024-06-01', 3), -- HR Analytics Intern

-- Student 15 (Amelia Garcia) - Chemical Engineering major
(15, 43, '2024-01-01', '2024-06-01', 4), -- Manufacturing Engineer

-- Student 18 (Alexander Lee) - Electrical Engineering major
(18, 45, '2024-01-01', '2024-06-01', 5), -- Automation Engineer

-- Student 21 (Aria Allen) - Marketing major
(21, 36, '2024-01-01', '2024-06-01', 3), -- Sales Analytics Intern

-- Student 24 (Grayson Wright) - Cybersecurity major
(24, 32, '2024-01-01', '2024-06-01', 5), -- Security Analyst Co-op

-- Student 30 (Jack Baker) - Computer Science major
(30, 22, '2024-01-01', '2024-06-01', 4), -- Backend Developer Intern

-- Additional past experiences (ensuring chronological order and major alignment)
(2, 50, '2021-06-01', '2021-12-01', 4), -- Business Development (business major)
(5, 46, '2021-09-01', '2022-03-01', 3), -- Customer Success Intern (marketing related)
(8, 42, '2021-09-01', '2022-03-01', 4), -- HR Analytics Intern (business related)
(11, 31, '2021-09-01', '2022-03-01', 5), -- Web Developer Intern (CS major)
(14, 41, '2021-09-01', '2022-03-01', 4), -- Network Engineer Co-op (IS major)
(17, 38, '2022-06-01', '2022-12-01', 3), -- Technical Writer (design/communication)
(20, 40, '2021-09-01', '2022-03-01', 5), -- AI Research Intern (data science)
(23, 42, '2022-06-01', '2022-12-01', 3), -- HR Analytics Intern (business)
(26, 49, '2022-09-01', '2023-03-01', 4), -- Infrastructure Engineer (IS major)
(29, 39, '2022-09-01', '2023-03-01', 4), -- Blockchain Developer (design/tech)

-- More chronological experiences
(1, 31, '2023-06-01', '2023-12-01', 4), -- Web Developer Intern (CS major)
(4, 37, '2023-06-01', '2023-12-01', 5), -- IoT Developer Co-op (data science/tech)
(6, 49, '2023-06-01', '2023-12-01', 4), -- Infrastructure Engineer (cybersecurity)
(9, 46, '2023-06-01', '2023-12-01', 3), -- Customer Success Intern (psychology)
(12, 42, '2022-06-01', '2022-12-01', 4), -- HR Analytics Intern (business)
(15, 25, '2023-06-01', '2023-12-01', 4), -- Research Assistant (chemical eng)
(18, 43, '2023-06-01', '2023-12-01', 4), -- Manufacturing Engineer (electrical eng)
(21, 44, '2023-06-01', '2023-12-01', 2), -- Content Creator Co-op (marketing)
(24, 41, '2023-06-01', '2023-12-01', 5), -- Network Engineer Co-op (cybersecurity)
(30, 1, '2023-06-01', '2023-12-01', 4), -- Software Developer Intern (CS major)

-- Final chronological entries
(4, 2, '2022-09-01', '2023-03-01', 5), -- Data Analyst Co-op (data science)
(6, 4, '2022-09-01', '2023-03-01', 5), -- Cybersecurity Intern
(9, 10, '2022-09-01', '2023-03-01', 3), -- Business Analyst Co-op (psychology/business)
(15, 7, '2022-09-01', '2023-03-01', 4), -- Biotech Research Co-op (chemical eng)
(18, 18, '2022-09-01', '2023-03-01', 5), -- Robotics Engineer Intern (electrical eng)
(21, 19, '2022-09-01', '2023-03-01', 3), -- Digital Marketing Co-op (marketing)
(30, 34, '2022-09-01', '2023-03-01', 4); -- Android Developer (CS major)

-- Views Position relationships (125 rows - bridge table for student interest)
INSERT INTO viewsPos (studentId, coopPositionId, preference) VALUES
-- Current students viewing current and future positions
(1, 1, TRUE), (1, 2, FALSE), (1, 16, TRUE), (1, 22, FALSE), (1, 31, TRUE),
(2, 5, TRUE), (2, 23, FALSE), (2, 27, TRUE), (2, 10, FALSE), (2, 50, TRUE),
(3, 8, TRUE), (3, 18, FALSE), (3, 43, TRUE), (3, 45, FALSE), (3, 49, TRUE),
(4, 2, TRUE), (4, 11, TRUE), (4, 29, TRUE), (4, 40, TRUE), (4, 47, FALSE),
(5, 3, FALSE), (5, 19, TRUE), (5, 36, FALSE), (5, 44, TRUE), (5, 46, FALSE),
(6, 4, TRUE), (6, 9, TRUE), (6, 32, TRUE), (6, 37, FALSE), (6, 41, TRUE),
(7, 7, TRUE), (7, 15, FALSE), (7, 25, TRUE), (7, 38, FALSE), (7, 42, FALSE),
(8, 5, FALSE), (8, 23, TRUE), (8, 27, FALSE), (8, 33, TRUE), (8, 39, FALSE),
(9, 3, FALSE), (9, 19, FALSE), (9, 42, TRUE), (9, 46, TRUE), (9, 36, FALSE),
(10, 8, TRUE), (10, 18, TRUE), (10, 43, FALSE), (10, 45, TRUE), (10, 49, FALSE),
(11, 1, TRUE), (11, 16, TRUE), (11, 22, FALSE), (11, 31, TRUE), (11, 34, FALSE),
(12, 10, FALSE), (12, 23, TRUE), (12, 30, FALSE), (12, 33, TRUE), (12, 50, TRUE),
(13, 8, TRUE), (13, 13, FALSE), (13, 21, TRUE), (13, 41, FALSE), (13, 49, TRUE),
(14, 4, FALSE), (14, 14, TRUE), (14, 26, FALSE), (14, 35, TRUE), (14, 41, FALSE),
(15, 7, TRUE), (15, 15, FALSE), (15, 25, TRUE), (15, 43, FALSE), (15, 45, TRUE),
(16, 1, TRUE), (16, 16, FALSE), (16, 22, TRUE), (16, 31, FALSE), (16, 34, TRUE),
(17, 6, FALSE), (17, 17, TRUE), (17, 38, FALSE), (17, 44, TRUE), (17, 48, TRUE),
(18, 9, TRUE), (18, 18, FALSE), (18, 32, TRUE), (18, 41, FALSE), (18, 45, TRUE),
(19, 3, FALSE), (19, 19, TRUE), (19, 36, FALSE), (19, 42, TRUE), (19, 50, FALSE),
(20, 2, TRUE), (20, 11, TRUE), (20, 29, FALSE), (20, 40, TRUE), (20, 47, TRUE),
(21, 3, TRUE), (21, 19, FALSE), (21, 36, TRUE), (21, 44, FALSE), (21, 46, TRUE),
(22, 1, FALSE), (22, 16, TRUE), (22, 22, FALSE), (22, 31, TRUE), (22, 34, FALSE),
(23, 5, TRUE), (23, 23, FALSE), (23, 27, TRUE), (23, 33, FALSE), (23, 50, TRUE),
(24, 4, TRUE), (24, 9, FALSE), (24, 32, TRUE), (24, 37, TRUE), (24, 41, FALSE),
(25, 7, FALSE), (25, 15, TRUE), (25, 25, FALSE), (25, 38, TRUE), (25, 42, FALSE),
(26, 14, TRUE), (26, 26, FALSE), (26, 35, TRUE), (26, 41, FALSE), (26, 49, TRUE),
(27, 8, FALSE), (27, 13, TRUE), (27, 21, FALSE), (27, 41, TRUE), (27, 49, FALSE),
(28, 10, TRUE), (28, 18, FALSE), (28, 30, TRUE), (28, 43, FALSE), (28, 45, TRUE),
(29, 6, TRUE), (29, 17, FALSE), (29, 38, TRUE), (29, 44, FALSE), (29, 48, TRUE),
(30, 1, FALSE), (30, 16, TRUE), (30, 22, FALSE), (30, 31, TRUE), (30, 34, FALSE);

-- Creates Position relationships (50 rows - bridge table for employers creating positions)
INSERT INTO createsPos (employerId, coopPositionId) VALUES
(37, 1), (37, 16), (37, 22), (37, 31), (37, 34),
(38, 2), (38, 11), (38, 29), (38, 40), (38, 47),
(39, 8), (39, 13), (39, 21), (39, 41), (39, 49),
(40, 7), (40, 15), (40, 25), (40, 38), (40, 42),
(41, 5), (41, 23), (41, 27), (41, 33), (41, 39),
(42, 6), (42, 12), (42, 18), (42, 43), (42, 45),
(43, 4), (43, 9), (43, 32), (43, 37), (43, 41),
(44, 7), (44, 15), (44, 25), (44, 38), (44, 42),
(37, 3), (37, 17), (37, 19), (37, 44), (37, 48),
(38, 10), (38, 13), (38, 30), (38, 46), (38, 50),
(39, 14), (40, 20), (41, 26), (42, 28), (43, 35),
(44, 24), (37, 36), (38, 39), (39, 44), (40, 42);

-- Applications table (60 rows - weak entity)
INSERT INTO applications (applicationId, dateTimeApplied, status, resume, gpa, coverLetter, coopPositionId) VALUES
(1, '2025-01-15 10:30:00', 'Submitted', 'Resume content for Emma Johnson...', 3.7, 'Cover letter expressing interest in software development...', 1),
(2, '2025-01-16 14:20:00', 'Under Review', 'Resume content for Emma Johnson...', 3.7, 'Cover letter for data analyst position...', 2),
(3, '2025-01-18 09:45:00', 'Submitted', 'Resume content for Liam Williams...', 3.5, 'Cover letter highlighting business experience...', 5),
(4, '2025-01-20 16:15:00', 'Draft', 'Resume content for Sophia Brown...', 3.8, NULL, 8),
(5, '2025-01-22 11:30:00', 'Submitted', 'Resume content for Noah Davis...', 3.9, 'Cover letter for data science role...', 11),
(6, '2025-01-25 08:45:00', 'Under Review', 'Resume content for Olivia Miller...', 3.4, 'Marketing position cover letter...', 3),
(7, '2025-01-28 13:20:00', 'Submitted', 'Resume content for Mason Wilson...', 3.6, 'Cybersecurity interest cover letter...', 4),
(8, '2025-01-30 10:00:00', 'Rejected', 'Resume content for Ava Moore...', 3.7, 'Biotech research application...', 7),
(9, '2025-02-01 15:30:00', 'Draft', 'Resume content for Ethan Taylor...', 3.8, NULL, 23),
(10, '2025-02-03 12:45:00', 'Submitted', 'Resume content for Isabella Anderson...', 3.3, 'HR analytics interest...', 42),
(11, '2025-02-05 09:15:00', 'Under Review', 'Resume content for James Thomas...', 3.5, 'Manufacturing engineering application...', 18),
(12, '2025-02-07 14:00:00', 'Submitted', 'Resume content for Mia Jackson...', 3.9, 'Full stack development interest...', 16),
(13, '2025-02-08 11:20:00', 'Draft', 'Resume content for Lucas White...', 3.4, NULL, 10),
(14, '2025-02-10 16:45:00', 'Submitted', 'Resume content for Charlotte Harris...', 3.6, 'Environmental focus application...', 21),
(15, '2025-02-12 08:30:00', 'Under Review', 'Resume content for Benjamin Martin...', 3.7, 'Systems administration interest...', 26),
(16, '2025-02-14 13:15:00', 'Submitted', 'Resume content for Amelia Garcia...', 3.5, 'Chemical engineering application...', 45),
(17, '2025-02-16 10:45:00', 'Draft', 'Resume content for Henry Rodriguez...', 3.2, NULL, 22),
(18, '2025-02-18 15:20:00', 'Submitted', 'Resume content for Harper Lewis...', 3.8, 'UX design passion letter...', 6),
(19, '2025-02-20 12:00:00', 'Under Review', 'Resume content for Alexander Lee...', 3.6, 'DevOps interest application...', 9),
(20, '2025-02-22 09:30:00', 'Submitted', 'Resume content for Evelyn Walker...', 3.4, 'International business focus...', 50),
(21, '2025-01-17 14:30:00', 'Submitted', 'Resume content for Sebastian Hall...', 3.8, 'ML engineering application...', 11),
(22, '2025-01-19 11:15:00', 'Under Review', 'Resume content for Aria Allen...', 3.3, 'Marketing coordinator interest...', 19),
(23, '2025-01-21 16:00:00', 'Draft', 'Resume content for Owen Young...', 3.1, NULL, 31),
(24, '2025-01-23 13:45:00', 'Submitted', 'Resume content for Luna King...', 3.7, 'Finance analyst application...', 27),
(25, '2025-01-26 10:20:00', 'Under Review', 'Resume content for Grayson Wright...', 3.5, 'Security analyst interest...', 32),
(26, '2025-01-29 15:10:00', 'Submitted', 'Resume content for Chloe Lopez...', 3.6, 'Bioengineering research focus...', 25),
(27, '2025-02-02 08:50:00', 'Draft', 'Resume content for Carter Hill...', 3.4, NULL, 35),
(28, '2025-02-04 12:30:00', 'Submitted', 'Resume content for Zoey Scott...', 3.7, 'Environmental engineering passion...', 49),
(29, '2025-02-06 14:40:00', 'Under Review', 'Resume content for Luke Green...', 3.3, 'Mechanical engineering application...', 43),
(30, '2025-02-09 11:55:00', 'Submitted', 'Resume content for Lily Adams...', 3.9, 'Product design interest...', 48),
(31, '2025-02-11 16:25:00', 'Draft', 'Resume content for Jack Baker...', 3.5, NULL, 34),
(32, '2025-01-24 09:40:00', 'Submitted', 'Resume content for Emma Johnson...', 3.7, 'Backend development interest...', 22),
(33, '2025-01-27 14:55:00', 'Under Review', 'Resume content for Liam Williams...', 3.5, 'Business intelligence focus...', 23),
(34, '2025-01-31 10:35:00', 'Submitted', 'Resume content for Sophia Brown...', 3.8, 'Infrastructure engineering...', 49),
(35, '2025-02-13 13:20:00', 'Draft', 'Resume content for Noah Davis...', 3.9, NULL, 29),
(36, '2025-02-15 08:15:00', 'Submitted', 'Resume content for Olivia Miller...', 3.4, 'Customer success application...', 46),
(37, '2025-02-17 15:45:00', 'Under Review', 'Resume content for Mason Wilson...', 3.6, 'Network engineering interest...', 41),
(38, '2025-02-19 12:10:00', 'Submitted', 'Resume content for Ava Moore...', 3.7, 'Research assistant focus...', 25),
(39, '2025-02-21 09:25:00', 'Draft', 'Resume content for Ethan Taylor...', 3.8, NULL, 39),
(40, '2025-01-14 16:30:00', 'Submitted', 'Resume content for Isabella Anderson...', 3.3, 'Content creation interest...', 44),
(41, '2025-01-16 11:45:00', 'Under Review', 'Resume content for James Thomas...', 3.5, 'Automation engineering...', 45),
(42, '2025-01-18 14:20:00', 'Submitted', 'Resume content for Mia Jackson...', 3.9, 'Android development passion...', 34),
(43, '2025-01-20 10:05:00', 'Draft', 'Resume content for Lucas White...', 3.4, NULL, 33),
(44, '2025-01-22 15:35:00', 'Submitted', 'Resume content for Charlotte Harris...', 3.6, 'Computer vision interest...', 47),
(45, '2025-01-25 12:50:00', 'Under Review', 'Resume content for Benjamin Martin...', 3.7, 'Database administration...', 35),
(46, '2025-01-28 08:40:00', 'Submitted', 'Resume content for Amelia Garcia...', 3.5, 'Manufacturing process focus...', 43),
(47, '2025-01-30 13:25:00', 'Draft', 'Resume content for Henry Rodriguez...', 3.2, NULL, 1),
(48, '2025-02-01 16:15:00', 'Submitted', 'Resume content for Harper Lewis...', 3.8, 'Technical writing interest...', 38),
(49, '2025-02-03 11:00:00', 'Under Review', 'Resume content for Alexander Lee...', 3.6, 'IoT development passion...', 37),
(50, '2025-02-05 14:45:00', 'Submitted', 'Resume content for Evelyn Walker...', 3.4, 'Business development focus...', 50),
(51, '2025-02-07 09:30:00', 'Draft', 'Resume content for Sebastian Hall...', 3.8, NULL, 40),
(52, '2025-02-10 12:15:00', 'Submitted', 'Resume content for Aria Allen...', 3.3, 'Sales analytics application...', 36),
(53, '2025-02-12 15:50:00', 'Under Review', 'Resume content for Owen Young...', 3.1, 'Web development interest...', 31),
(54, '2025-02-14 10:25:00', 'Submitted', 'Resume content for Luna King...', 3.7, 'Project coordination focus...', 30),
(55, '2025-02-16 13:40:00', 'Draft', 'Resume content for Grayson Wright...', 3.5, NULL, 4),
(56, '2025-02-18 08:55:00', 'Submitted', 'Resume content for Chloe Lopez...', 3.6, 'Healthcare data analysis...', 15),
(57, '2025-02-20 14:10:00', 'Under Review', 'Resume content for Carter Hill...', 3.4, 'QA engineering interest...', 17),
(58, '2025-02-22 11:35:00', 'Submitted', 'Resume content for Zoey Scott...', 3.7, 'Cloud engineering passion...', 20),
(59, '2025-01-13 16:20:00', 'Draft', 'Resume content for Luke Green...', 3.3, NULL, 28),
(60, '2025-01-15 12:45:00', 'Submitted', 'Resume content for Lily Adams...', 3.9, 'Game development interest...', 14);

-- Applies To App relationships (60 rows - bridge table)
INSERT INTO appliesToApp (applicationId, studentId) VALUES
(1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9),
(11, 10), (12, 11), (13, 12), (14, 13), (15, 14), (16, 15), (17, 16), (18, 17), (19, 18), (20, 19),
(21, 20), (22, 21), (23, 22), (24, 23), (25, 24), (26, 25), (27, 26), (28, 27), (29, 28), (30, 29),
(31, 30), (32, 1), (33, 2), (34, 3), (35, 4), (36, 5), (37, 6), (38, 7), (39, 8), (40, 9),
(41, 10), (42, 11), (43, 12), (44, 13), (45, 14), (46, 15), (47, 16), (48, 17), (49, 18), (50, 19),
(51, 20), (52, 21), (53, 22), (54, 23), (55, 24), (56, 25), (57, 26), (58, 27), (59, 28), (60, 29);

-- Reviews App relationships (125 rows - bridge table for employers reviewing applications)
INSERT INTO reviewsApp (applicationId, employerId, flag) VALUES
-- Applications reviewed by employers who created those positions
-- Application 1 (coopPositionId 1) - created by employer 37
(1, 37, FALSE),
-- Application 2 (coopPositionId 2) - created by employer 38
(2, 38, FALSE),
-- Application 3 (coopPositionId 5) - created by employer 41
(3, 41, FALSE),
-- Application 4 (coopPositionId 8) - created by employer 39
(4, 39, FALSE),
-- Application 5 (coopPositionId 11) - created by employer 38
(5, 38, FALSE),
-- Application 6 (coopPositionId 3) - created by employer 37
(6, 37, FALSE),
-- Application 7 (coopPositionId 4) - created by employer 43
(7, 43, FALSE),
-- Application 8 (coopPositionId 7) - created by employer 40 and 44
(8, 40, FALSE), (8, 44, FALSE),
-- Application 9 (coopPositionId 23) - created by employer 41
(9, 41, FALSE),
-- Application 10 (coopPositionId 42) - created by employer 40
(10, 40, FALSE),
-- Application 11 (coopPositionId 18) - created by employer 42
(11, 42, FALSE),
-- Application 12 (coopPositionId 16) - created by employer 37
(12, 37, FALSE),
-- Application 13 (coopPositionId 10) - created by employer 38
(13, 38, FALSE),
-- Application 14 (coopPositionId 21) - created by employer 39
(14, 39, FALSE),
-- Application 15 (coopPositionId 26) - created by employer 39
(15, 39, FALSE),
-- Application 16 (coopPositionId 45) - created by employer 42
(16, 42, FALSE),
-- Application 17 (coopPositionId 22) - created by employer 37
(17, 37, FALSE),
-- Application 18 (coopPositionId 6) - created by employer 42
(18, 42, FALSE),
-- Application 19 (coopPositionId 9) - created by employer 43
(19, 43, FALSE),
-- Application 20 (coopPositionId 50) - created by employer 38
(20, 38, FALSE),
-- Application 21 (coopPositionId 11) - created by employer 38
(21, 38, FALSE),
-- Application 22 (coopPositionId 19) - created by employer 37
(22, 37, FALSE),
-- Application 23 (coopPositionId 31) - created by employer 37
(23, 37, FALSE),
-- Application 24 (coopPositionId 27) - created by employer 41
(24, 41, FALSE),
-- Application 25 (coopPositionId 32) - created by employer 43
(25, 43, FALSE),
-- Application 26 (coopPositionId 25) - created by employer 40 and 44
(26, 40, FALSE), (26, 44, FALSE),
-- Application 27 (coopPositionId 35) - created by employer 41
(27, 41, FALSE),
-- Application 28 (coopPositionId 49) - created by employer 39
(28, 39, FALSE),
-- Application 29 (coopPositionId 43) - created by employer 42
(29, 42, FALSE),
-- Application 30 (coopPositionId 48) - created by employer 37
(30, 37, FALSE),
-- Application 31 (coopPositionId 34) - created by employer 37
(31, 37, FALSE),
-- Application 32 (coopPositionId 22) - created by employer 37
(32, 37, FALSE),
-- Application 33 (coopPositionId 23) - created by employer 41
(33, 41, FALSE),
-- Application 34 (coopPositionId 49) - created by employer 39
(34, 39, FALSE),
-- Application 35 (coopPositionId 29) - created by employer 38
(35, 38, FALSE),
-- Application 36 (coopPositionId 46) - created by employer 38
(36, 38, FALSE),
-- Application 37 (coopPositionId 41) - created by employer 39 and 43
(37, 39, FALSE), (37, 43, FALSE),
-- Application 38 (coopPositionId 25) - created by employer 40 and 44
(38, 40, FALSE), (38, 44, FALSE),
-- Application 39 (coopPositionId 39) - created by employer 41
(39, 41, FALSE),
-- Application 40 (coopPositionId 44) - created by employer 37 and 39
(40, 37, FALSE), (40, 39, FALSE),
-- Application 41 (coopPositionId 45) - created by employer 42
(41, 42, FALSE),
-- Application 42 (coopPositionId 34) - created by employer 37
(42, 37, FALSE),
-- Application 43 (coopPositionId 33) - created by employer 41
(43, 41, FALSE),
-- Application 44 (coopPositionId 47) - created by employer 38
(44, 38, FALSE),
-- Application 45 (coopPositionId 35) - created by employer 41
(45, 41, FALSE),
-- Application 46 (coopPositionId 43) - created by employer 42
(46, 42, FALSE),
-- Application 47 (coopPositionId 1) - created by employer 37
(47, 37, FALSE),
-- Application 48 (coopPositionId 38) - created by employer 40 and 44
(48, 40, FALSE), (48, 44, FALSE),
-- Application 49 (coopPositionId 37) - created by employer 43
(49, 43, FALSE),
-- Application 50 (coopPositionId 50) - created by employer 38
(50, 38, FALSE),
-- Application 51 (coopPositionId 40) - created by employer 38
(51, 38, FALSE),
-- Application 52 (coopPositionId 36) - created by employer 37
(52, 37, FALSE),
-- Application 53 (coopPositionId 31) - created by employer 37
(53, 37, FALSE),
-- Application 54 (coopPositionId 30) - created by employer 38
(54, 38, FALSE),
-- Application 55 (coopPositionId 4) - created by employer 43
(55, 43, FALSE),
-- Application 56 (coopPositionId 15) - created by employer 40 and 44
(56, 40, FALSE), (56, 44, FALSE),
-- Application 57 (coopPositionId 17) - created by employer 37
(57, 37, FALSE),
-- Application 58 (coopPositionId 20) - created by employer 38
(58, 38, FALSE),
-- Application 59 (coopPositionId 28) - created by employer 41
(59, 41, FALSE),
-- Application 60 (coopPositionId 14) - created by employer 39
(60, 39, FALSE),
-- Additional reviews from the same employers for positions they created
(1, 38, FALSE), (2, 37, FALSE), (3, 40, FALSE), (4, 38, FALSE), (5, 37, FALSE),
(6, 38, FALSE), (7, 40, FALSE), (9, 38, FALSE), (10, 44, FALSE), (11, 43, FALSE),
(12, 38, FALSE), (13, 40, FALSE), (14, 40, FALSE), (15, 40, FALSE), (16, 43, FALSE),
(17, 38, FALSE), (18, 43, FALSE), (19, 40, FALSE), (20, 37, FALSE), (21, 37, FALSE),
(22, 38, FALSE), (23, 38, FALSE), (24, 40, FALSE), (25, 40, FALSE), (27, 40, FALSE),
(28, 40, FALSE), (29, 43, FALSE), (30, 38, FALSE), (31, 38, FALSE), (32, 38, FALSE),
(33, 40, FALSE), (34, 40, FALSE), (35, 37, FALSE), (36, 37, FALSE), (39, 40, FALSE),
(41, 43, FALSE), (42, 38, FALSE), (43, 40, FALSE), (44, 37, FALSE), (45, 40, FALSE),
(46, 43, FALSE), (47, 38, FALSE), (50, 37, FALSE), (51, 37, FALSE), (52, 38, FALSE),
(53, 38, FALSE), (54, 37, FALSE), (55, 40, FALSE), (57, 38, FALSE), (58, 37, FALSE),
(59, 40, FALSE), (60, 40, FALSE);