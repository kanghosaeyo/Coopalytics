USE coopalytics;

-- 1. Skills table (40 rows - strong entity, no dependencies)
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

-- 2. Company Profiles table (35 rows - strong entity, no dependencies)
INSERT INTO companyProfiles (companyProfileId, name, bio, industry, websiteLink) VALUES
(1, 'TechNova Inc', 'Leading software development company specializing in enterprise solutions and cloud infrastructure.', 'Technology', 'www.technova.com'),
(2, 'DataFlow Analytics', 'Data science consulting firm helping businesses make data-driven decisions through advanced analytics.', 'Technology', 'www.dataflow.com'),
(3, 'GreenTech Solutions', 'Environmental technology company focused on sustainable energy and green infrastructure solutions.', 'Environmental', 'www.greentech.com'),
(4, 'FinanceFirst Corp', 'Financial services company providing investment management and banking solutions to corporate clients.', 'Finance', 'www.financefirst.com'),
(5, 'HealthTech Innovations', 'Healthcare technology startup developing AI-powered diagnostic tools and patient management systems.', 'Healthcare', 'www.healthtech.com'),
(6, 'CyberShield Security', 'Cybersecurity firm specializing in threat detection, incident response, and security consulting services.', 'Technology', 'www.cybershield.com'),
(7, 'BioResearch Labs', 'Biotechnology research company focused on drug discovery and medical device development.', 'Healthcare', 'www.bioresearch.com'),
(8, 'CloudFirst Technologies', 'Cloud infrastructure provider offering scalable solutions for enterprise digital transformation.', 'Technology', 'www.cloudfirst.com'),
(9, 'MarketPulse Agency', 'Digital marketing agency specializing in social media strategy and content marketing campaigns.', 'Marketing', 'www.marketpulse.com'),
(10, 'AutoMech Industries', 'Manufacturing company specializing in automotive parts and industrial automation systems.', 'Manufacturing', 'www.automech.com'),
(11, 'EduTech Platform', 'Educational technology company developing online learning platforms and student management systems.', 'Education', 'www.edutech.com'),
(12, 'RetailMax Solutions', 'Retail technology provider offering point-of-sale systems and inventory management solutions.', 'Retail', 'www.retailmax.com'),
(13, 'EnergyFlow Corp', 'Renewable energy company focused on solar and wind power generation and distribution systems.', 'Energy', 'www.energyflow.com'),
(14, 'LogiTrans Systems', 'Logistics and transportation company providing supply chain management and delivery solutions.', 'Logistics', 'www.logitrans.com'),
(15, 'DesignStudio Pro', 'Creative design agency specializing in brand identity, web design, and user experience consulting.', 'Design', 'www.designstudio.com'),
(16, 'AgriTech Innovations', 'Agricultural technology company developing precision farming tools and crop management systems.', 'Agriculture', 'www.agritech.com'),
(17, 'SportsTech Analytics', 'Sports technology company providing performance analytics and fan engagement platforms.', 'Sports', 'www.sportstech.com'),
(18, 'MediaStream Corp', 'Media and entertainment company specializing in streaming platforms and content distribution.', 'Media', 'www.mediastream.com'),
(19, 'RealEstate Plus', 'Real estate technology company offering property management and virtual tour solutions.', 'Real Estate', 'www.realestate.com'),
(20, 'TravelTech Solutions', 'Travel technology provider developing booking platforms and travel management systems.', 'Travel', 'www.traveltech.com'),
(21, 'FoodTech Innovations', 'Food technology company focused on sustainable food production and delivery optimization.', 'Food', 'www.foodtech.com'),
(22, 'InsureTech Corp', 'Insurance technology company providing digital insurance platforms and risk assessment tools.', 'Insurance', 'www.insuretech.com'),
(23, 'GameDev Studios', 'Video game development company creating mobile and console games with immersive experiences.', 'Gaming', 'www.gamedev.com'),
(24, 'LegalTech Solutions', 'Legal technology provider offering case management systems and document automation tools.', 'Legal', 'www.legaltech.com'),
(25, 'ConstructTech Pro', 'Construction technology company providing project management and building information modeling.', 'Construction', 'www.constructtech.com'),
(26, 'PharmaResearch Inc', 'Pharmaceutical research company focused on drug development and clinical trial management.', 'Pharmaceutical', 'www.pharmaresearch.com'),
(27, 'AeroSpace Dynamics', 'Aerospace engineering company developing aircraft systems and space exploration technologies.', 'Aerospace', 'www.aerospace.com'),
(28, 'TextileTech Corp', 'Textile manufacturing company specializing in smart fabrics and sustainable clothing production.', 'Textile', 'www.textiletech.com'),
(29, 'MiningTech Solutions', 'Mining technology provider offering equipment automation and resource extraction optimization.', 'Mining', 'www.miningtech.com'),
(30, 'WaterTech Systems', 'Water technology company developing purification systems and water resource management solutions.', 'Water', 'www.watertech.com'),
(31, 'RoboTech Industries', 'Robotics company creating industrial automation solutions and service robots for various sectors.', 'Robotics', 'www.robotech.com'),
(32, 'ChemTech Labs', 'Chemical technology company specializing in materials science and chemical process optimization.', 'Chemical', 'www.chemtech.com'),
(33, 'TransportTech Corp', 'Transportation technology provider developing autonomous vehicle systems and traffic management.', 'Transportation', 'www.transporttech.com'),
(34, 'SecurityTech Pro', 'Physical security technology company offering surveillance systems and access control solutions.', 'Security', 'www.securitytech.com'),
(35, 'CleanTech Innovations', 'Clean technology company focused on waste management and environmental remediation solutions.', 'Environmental', 'www.cleantech.com');

-- 3. Users table (48 rows - references companyProfiles)
INSERT INTO users (userId, firstName, lastName, email, phone, major, minor, college, gradYear, grade, companyProfileId, industry) VALUES
-- Students (userId 1-30) 
(1, 'Charlie', 'Stout', 'c.stout@student.edu', '555-0101', 'Computer Science', 'Mathematics', 'Khoury College of Computer Sciences', '2026', 'Junior', NULL, NULL),
(2, 'Liam', 'Williams', 'l.williams@student.edu', '555-0102', 'Business', 'Economics', 'D\'Amore-McKim School of Business', '2025', 'Senior', NULL, NULL),
(3, 'Sophia', 'Brown', 's.brown@student.edu', '555-0103', 'Mechanical Engineering', 'Physics', 'College of Engineering', '2027', 'Sophomore', NULL, NULL),
(4, 'Noah', 'Davis', 'n.davis@student.edu', '555-0104', 'Data Science', NULL, 'Khoury College of Computer Sciences', '2026', 'Junior', NULL, NULL),
(5, 'Olivia', 'Miller', 'o.miller@student.edu', '555-0105', 'Marketing', 'Psychology', 'D\'Amore-McKim School of Business', '2025', 'Senior', NULL, NULL),
(6, 'Mason', 'Wilson', 'm.wilson@student.edu', '555-0106', 'Cybersecurity', NULL, 'Khoury College of Computer Sciences', '2026', 'Junior', NULL, NULL),
(7, 'Ava', 'Moore', 'a.moore@student.edu', '555-0107', 'Biomedical Engineering', 'Chemistry', 'College of Engineering', '2027', 'Sophomore', NULL, NULL),
(8, 'Ethan', 'Taylor', 'e.taylor@student.edu', '555-0108', 'Finance', NULL, 'D\'Amore-McKim School of Business', '2025', 'Senior', NULL, NULL),
(9, 'Isabella', 'Anderson', 'i.anderson@student.edu', '555-0109', 'Psychology', 'Sociology', 'College of Social Sciences and Humanities', '2026', 'Junior', NULL, NULL),
(10, 'James', 'Thomas', 'j.thomas@student.edu', '555-0110', 'Mechanical Engineering', NULL, 'College of Engineering', '2027', 'Sophomore', NULL, NULL),
(11, 'Mia', 'Jackson', 'm.jackson@student.edu', '555-0111', 'Computer Science', NULL, 'Khoury College of Computer Sciences', '2025', 'Senior', NULL, NULL),
(12, 'Lucas', 'White', 'l.white@student.edu', '555-0112', 'Business', 'Data Science', 'D\'Amore-McKim School of Business', '2026', 'Junior', NULL, NULL),
(13, 'Charlotte', 'Harris', 'c.harris@student.edu', '555-0113', 'Environmental Engineering', 'Biology', 'College of Engineering', '2027', 'Sophomore', NULL, NULL),
(14, 'Benjamin', 'Martin', 'b.martin@student.edu', '555-0114', 'Information Systems', NULL, 'Khoury College of Computer Sciences', '2025', 'Senior', NULL, NULL),
(15, 'Amelia', 'Garcia', 'a.garcia@student.edu', '555-0115', 'Physics', 'Mathematics', 'College of Science', '2026', 'Junior', NULL, NULL),
(16, 'Henry', 'Rodriguez', 'h.rodriguez@student.edu', '555-0116', 'Computer Science', 'Mathematics', 'Khoury College of Computer Sciences', '2027', 'Sophomore', NULL, NULL),
(17, 'Harper', 'Lewis', 'h.lewis@student.edu', '555-0117', 'Design', 'Art', 'College of Arts, Media and Design', '2025', 'Senior', NULL, NULL),
(18, 'Alexander', 'Lee', 'a.lee@student.edu', '555-0118', 'Electrical Engineering', NULL, 'College of Engineering', '2026', 'Junior', NULL, NULL),
(19, 'Evelyn', 'Walker', 'e.walker@student.edu', '555-0119', 'International Business', 'Spanish', 'D\'Amore-McKim School of Business', '2027', 'Sophomore', NULL, NULL),
(20, 'Sebastian', 'Hall', 's.hall@student.edu', '555-0120', 'Data Science', NULL, 'Khoury College of Computer Sciences', '2025', 'Senior', NULL, NULL),
(21, 'Aria', 'Allen', 'a.allen@student.edu', '555-0121', 'Marketing', NULL, 'D\'Amore-McKim School of Business', '2026', 'Junior', NULL, NULL),
(22, 'Owen', 'Young', 'o.young@student.edu', '555-0122', 'Computer Science', NULL, 'Khoury College of Computer Sciences', '2027', 'Sophomore', NULL, NULL),
(23, 'Luna', 'King', 'l.king@student.edu', '555-0123', 'Business', 'Finance', 'D\'Amore-McKim School of Business', '2025', 'Senior', NULL, NULL),
(24, 'Grayson', 'Wright', 'g.wright@student.edu', '555-0124', 'Cybersecurity', NULL, 'Khoury College of Computer Sciences', '2026', 'Junior', NULL, NULL),
(25, 'Chloe', 'Lopez', 'c.lopez@student.edu', '555-0125', 'Biology', 'Chemistry', 'College of Science', '2027', 'Sophomore', NULL, NULL),
(26, 'Carter', 'Hill', 'c.hill@student.edu', '555-0126', 'Information Systems', 'Business', 'Khoury College of Computer Sciences', '2025', 'Senior', NULL, NULL),
(27, 'Zoey', 'Scott', 'z.scott@student.edu', '555-0127', 'Environmental Engineering', NULL, 'College of Engineering', '2026', 'Junior', NULL, NULL),
(28, 'Luke', 'Green', 'l.green@student.edu', '555-0128', 'Chemistry', 'Mathematics', 'College of Science', '2027', 'Sophomore', NULL, NULL),
(29, 'Lily', 'Adams', 'l.adams@student.edu', '555-0129', 'Design', NULL, 'College of Arts, Media and Design', '2025', 'Senior', NULL, NULL),
(30, 'Jack', 'Baker', 'j.baker@student.edu', '555-0130', 'Computer Science', NULL, 'Khoury College of Computer Sciences', '2026', 'Junior', NULL, NULL),
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

-- 4. Demographics table (48 rows - references users)
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

-- 5. Coop Positions table (50 rows - references skills)
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

-- 6. Applications table (60 rows - references coopPositions)
INSERT INTO applications (applicationId, dateTimeApplied, status, resume, gpa, coverLetter, coopPositionId) VALUES
-- Charlie Stout (CS major, GPA 3.7, has Python, Java, JavaScript, React, etc.)
(1, '2025-01-15 10:30:00', 'Submitted', 'Resume content for Charlie Stout...', 3.7, 'Cover letter expressing interest in software development...', 1),
(2, '2025-01-16 14:20:00', 'Under Review', 'Resume content for Charlie Stout...', 3.7, 'Cover letter for full stack developer...', 16),
-- Liam Williams (Business major, GPA 3.5, has Excel, PowerPoint, Project Management, etc.)
(3, '2025-01-18 09:45:00', 'Submitted', 'Resume content for Liam Williams...', 3.5, 'Cover letter highlighting business experience...', 5),
(4, '2025-01-20 16:15:00', 'Draft', 'Resume content for Liam Williams...', 3.5, NULL, 10),
-- Sophia Brown (Engineering major, GPA 3.8, has C++, Excel, Project Management, etc.)
(5, '2025-01-22 11:30:00', 'Submitted', 'Resume content for Sophia Brown...', 3.8, 'Cover letter for engineering role...', 18),
(6, '2025-01-25 08:45:00', 'Under Review', 'Resume content for Sophia Brown...', 3.8, 'Manufacturing engineering application...', 43),
-- Noah Davis (Data Science major, GPA 3.9, has Python, ML, Data Analysis, etc.)
(7, '2025-01-28 13:20:00', 'Submitted', 'Resume content for Noah Davis...', 3.9, 'Machine learning interest cover letter...', 11),
(8, '2025-01-30 10:00:00', 'Rejected', 'Resume content for Noah Davis...', 3.9, 'Data engineering application...', 29),
-- Olivia Miller (Marketing major, GPA 3.4, has Excel, PowerPoint, Communication, etc.)
(9, '2025-02-01 15:30:00', 'Draft', 'Resume content for Olivia Miller...', 3.4, NULL, 3),
(10, '2025-02-03 12:45:00', 'Submitted', 'Resume content for Olivia Miller...', 3.4, 'Digital marketing interest...', 19);

-- 7. Skill Details table (sample rows for testing - references skills and users)
INSERT INTO skillDetails (skillId, studentId, proficiencyLevel) VALUES
-- Student 1 (Charlie Stout) - Computer Science major
(1, 1, 4), (2, 1, 3), (3, 1, 5), (4, 1, 4), (5, 1, 3), (6, 1, 4), (10, 1, 5), (17, 1, 4), (19, 1, 4), (20, 1, 5),
-- Student 2 (Liam Williams) - Business major
(13, 2, 5), (14, 2, 4), (15, 2, 4), (16, 2, 3), (17, 2, 5), (18, 2, 4), (19, 2, 4), (20, 2, 5),
-- Student 3 (Sophia Brown) - Engineering major
(21, 3, 4), (13, 3, 4), (15, 3, 5), (19, 3, 4), (20, 3, 5), (17, 3, 3), (12, 3, 3),
-- Student 4 (Noah Davis) - Data Science major
(1, 4, 5), (11, 4, 5), (12, 4, 5), (37, 4, 4), (38, 4, 4), (6, 4, 4), (17, 4, 4), (19, 4, 5), (20, 4, 5),
-- Student 5 (Olivia Miller) - Marketing major
(13, 5, 4), (14, 5, 5), (17, 5, 5), (18, 5, 4), (19, 5, 4), (20, 5, 5), (12, 5, 3);

-- 7. Creates Position relationships (bridge table - references users and coopPositions)
INSERT INTO createsPos (employerId, coopPositionId) VALUES
(37, 1), (37, 2), (37, 3), (37, 4), (37, 5), (37, 6), (37, 7), (37, 8), (37, 9), (37, 10),
(38, 11), (38, 12), (38, 13), (38, 14), (38, 15), (38, 16), (38, 17), (38, 18), (38, 19), (38, 20),
(39, 21), (39, 22), (39, 23), (39, 24), (39, 25), (39, 26), (39, 27), (39, 28), (39, 29), (39, 30),
(40, 31), (40, 32), (40, 33), (40, 34), (40, 35), (40, 36), (40, 37), (40, 38), (40, 39), (40, 40),
(41, 41), (41, 42), (41, 43), (41, 44), (41, 45), (41, 46), (41, 47), (41, 48), (41, 49), (41, 50);

-- 7. Advisor-Advisee relationships (bridge table - references users)
INSERT INTO advisor_advisee (advisorId, studentId) VALUES
-- Sarah Martinez (advisor 31) advises students 1-10
(31, 1), (31, 2), (31, 3), (31, 4), (31, 5), (31, 6), (31, 7), (31, 8), (31, 9), (31, 10),
-- Michael Chen (advisor 32) advises students 11-20
(32, 11), (32, 12), (32, 13), (32, 14), (32, 15), (32, 16), (32, 17), (32, 18), (32, 19), (32, 20),
-- Jennifer Kim (advisor 33) advises students 21-30
(33, 21), (33, 22), (33, 23), (33, 24), (33, 25), (33, 26), (33, 27), (33, 28), (33, 29), (33, 30);

-- 8. Applies To App relationships (bridge table - references applications and users)
INSERT INTO appliesToApp (applicationId, studentId) VALUES
(1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4), (9, 5), (10, 5);

