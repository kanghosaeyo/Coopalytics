DROP DATABASE IF EXISTS `coopalytics`;
CREATE DATABASE `coopalytics`;
USE `coopalytics`;

CREATE TABLE skills (
    skillId  INT PRIMARY KEY,
    name     VARCHAR(20) NOT NULL,
    category VARCHAR(20) NOT NULL
);

CREATE TABLE companyProfiles (
    companyProfileId INT PRIMARY KEY,
    name             VARCHAR(20) NOT NULL,
    bio              LONGTEXT,
    industry         VARCHAR(20) NOT NULL,
    websiteLink      VARCHAR(50)
);

CREATE TABLE demographics (
    demographicId INT PRIMARY KEY,
    gender        VARCHAR(20),
    race          VARCHAR(20),
    nationality   VARCHAR(20),
    sexuality     VARCHAR(20),
    disability    VARCHAR(20)
);

CREATE TABLE users (
    userId           INT PRIMARY KEY,
    firstName        VARCHAR(20) NOT NULL,
    lastName         VARCHAR(20) NOT NULL,
    demographicId    INT,
    email            VARCHAR(20) NOT NULL,
    phone            VARCHAR(20),
    major            VARCHAR(20),
    minor            VARCHAR(20),
    college          VARCHAR(20),
    gradYear         VARCHAR(20),
    grade            VARCHAR(10),
    companyProfileId INT,
    industry         VARCHAR(20),

    FOREIGN KEY (demographicId) REFERENCES demographics (demographicId) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (companyProfileId) REFERENCES companyProfiles (companyProfileId) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE coopPositions (
    coopPositionId   INT PRIMARY KEY,
    title            VARCHAR(30) NOT NULL,
    location         VARCHAR(30) NOT NULL DEFAULT 'Not Specified',
    description      LONGTEXT    NOT NULL,
    hourlyPay        FLOAT       NOT NULL,
    requiredSkillsId INT,
    desiredSkillsId  INT,
    desiredGPA       FLOAT,
    deadline         DATETIME,
    startDate        DATE        NOT NULL,
    endDate          DATE        NOT NULL,
    flag             BOOLEAN     NOT NULL DEFAULT FALSE,
    industry         VARCHAR(30) NOT NULL DEFAULT 'Not Specified',

    FOREIGN KEY (requiredSkillsId) REFERENCES skills (skillId) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (desiredSkillsId) REFERENCES skills (skillId) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE skillDetails (
    skillId          INT,
    studentId        INT,
    proficiencyLevel INT NOT NULL,

    PRIMARY KEY (skillId, studentId),
    FOREIGN KEY (skillId) REFERENCES skills (skillId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (studentId) REFERENCES users (userId) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE advisor_advisee (
    studentId INT,
    advisorId INT,
    flag      BOOLEAN NOT NULL DEFAULT FALSE,

    PRIMARY KEY (studentId, advisorId),
    FOREIGN KEY (studentId) REFERENCES users (userId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (advisorId) REFERENCES users (userId) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE workedAtPos (
    studentId      INT,
    coopPositionId INT,
    startDate      DATE NOT NULL,
    endDate        DATE NOT NULL,
    companyRating  INT,

    PRIMARY KEY (studentId, coopPositionId),
    FOREIGN KEY (studentId) REFERENCES users (userId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (coopPositionId) REFERENCES coopPositions (coopPositionId) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE viewsPos (
    studentId      INT,
    coopPositionId INT,
    preference     BOOLEAN DEFAULT FALSE,

    PRIMARY KEY (studentId, coopPositionId),
    FOREIGN KEY (studentId) REFERENCES users (userId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (coopPositionId) REFERENCES coopPositions (coopPositionId) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE createsPos (
    employerId     INT,
    coopPositionId INT,

    PRIMARY KEY (employerId, coopPositionId),
    FOREIGN KEY (employerId) REFERENCES users (userId) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (coopPositionId) REFERENCES coopPositions (coopPositionId) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE applications (
    applicationId   INT PRIMARY KEY,
    dateTimeApplied DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status          VARCHAR(15) NOT NULL DEFAULT 'Draft',
    resume          LONGTEXT,
    gpa             FLOAT,
    coverLetter     LONGTEXT,
    coopPositionId  INT         NOT NULL,

    FOREIGN KEY (coopPositionId) REFERENCES coopPositions (coopPositionId) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE appliesToApp (
    applicationId INT,
    studentId INT,

    PRIMARY KEY (applicationId, studentId),
    FOREIGN KEY (applicationId) REFERENCES applications (applicationId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (studentId) REFERENCES users (userId) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE reviewsApp (
    applicationId INT,
    employerId    INT,
    flag          BOOLEAN NOT NULL DEFAULT FALSE,

    PRIMARY KEY (applicationId, employerId),
    FOREIGN KEY (applicationId) REFERENCES applications (applicationId) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (employerId) REFERENCES users (userId) ON UPDATE CASCADE ON DELETE CASCADE
);
