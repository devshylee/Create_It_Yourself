CREATE Table Users (
  Id INT PRIMARY KEY AUTO_INCREMENT,
  memberId  VARCHAR(100),
  memberPw VARCHAR(100),
  memberName VARCHAR(40),
  memberEmail VARCHAR(255) UNIQUE,
  memberBirthDate varchar(40),
  memberMobile varchar(40),
  created_at timestamp
);
CREATE Table Answer (
  AnswerId INT PRIMARY KEY AUTO_INCREMENT ,
  QuestionId INT ,
  Content VARCHAR(200) ,
  created_at timestamp
);
CREATE Table Question (
  QuestionId INT PRIMARY KEY AUTO_INCREMENT ,
  Content VARCHAR(200) ,
  created_at timestamp
);
CREATE Table Books (
  BookId INT PRIMARY KEY AUTO_INCREMENT,
  Content text,
  DiaryId int,
  UserId int,
  mm_yy varchar(20),
  ThemeId int
);
CREATE Table Theme (
  ThemeId INT PRIMARY KEY AUTO_INCREMENT,
  Content varchar(255)
);
CREATE Table Diarys (
  DiaryId INT PRIMARY KEY AUTO_INCREMENT,
  title varchar(100),
  Content text,
  week varchar(100),
  AnswerId int,
  ImageId int,
  created_at timestamp
);

CREATE Table Image (
  ImageId INT PRIMARY KEY AUTO_INCREMENT,
  ImagePath varchar(500)
);