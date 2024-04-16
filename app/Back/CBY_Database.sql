CREATE TABLE member_table(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    memberEmail VARCHAR(255) UNIQUE,
    memberPassword VARCHAR(255),
    memberName VARCHAR(255),
    signDate TIMESTAMP,
    memberBirthDate VARCHAR(255)
);

CREATE TABLE Question (
    QuestionID INTEGER PRIMARY KEY,
    Content VARCHAR(255)
);

CREATE TABLE Answer (
    AnswerID INTEGER PRIMARY KEY,
    member_id BIGINT,
    QuestionID INTEGER,
    Content VARCHAR(255),
    CreationDate TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES member_table(id),
    FOREIGN KEY (QuestionID) REFERENCES Question(QuestionID)
);

CREATE TABLE Image (
    ImageID INTEGER PRIMARY KEY,
    ImagePath VARCHAR(255)
);

CREATE TABLE Diary (
    DiaryID INTEGER PRIMARY KEY,
    member_id BIGINT,
    Content VARCHAR(255),
    CreationDate TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES member_table(id)
);
