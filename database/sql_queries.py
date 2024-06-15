CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE(TELEGRAM_ID)
)
"""

ALTER_TABLE_USER_TABLE_V1 = """
ALTER TABLE telegram_users ADD COLUMN REFERENCE_LINK TEXT
"""

ALTER_TABLE_USER_TABLE_V2 = """
ALTER TABLE telegram_users ADD COLUMN BALANCE INTEGER
"""

UPDATE_USER_BALANCE_COLUMN_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_LINK_COLUMN_QUERY = """
UPDATE telegram_users SET COALESCE(BALANCE, 0) + ? WHERE TELEGRAM_ID = ?
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES(?,?,?,?,?,?,?)
"""

SELECT_USER_QUERY = """
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
"""

SELECT_USER_BY_LINK_QUERY = """
SELECT * FROM telegram_users WHERE REFERENCE_LINK = ?
"""

UPDATE_USER_LINK_COLUMN_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_BALANCE_COLUMN_QUERY = """
UPDATE telegram_users SET BALANCE = 100 WHERE TELEGRAM_ID = ?
"""

CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profile
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIO TEXT,
PHOTO TEXT,
UNIQUE(TELEGRAM_ID)
)
"""

INSERT_PROFILE_QUERY = """
INSERT INTO profile VALUES(?,?,?,?,?)
"""

SELECT_PROFILE_QUERY = """
SELECT * FROM profile WHERE TELEGRAM_ID = ?
"""

CREATE_LIKE_DISLIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_dislike
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
LIKE_STATUS INTEGER,
UNIQUE(OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""

INSERT_LIKE_QUERY = """
INSERT INTO like_dislike VALUES(?,?,?,?)
"""

SELECT_ALL_PROFILES = """
SELECT * FROM profile p 
WHERE p.TELEGRAM_ID NOT IN (
    SELECT ld.OWNER_TELEGRAM_ID
    FROM like_dislike ld
    WHERE ld.LIKER_TELEGRAM_ID = ?
    AND ld.LIKE_STATUS IS NOT NULL
)
AND p.TELEGRAM_ID != ?
"""

CREATE_REFERENCE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS reference
(
ID INTEGER PRIMARY KEY,
INVITER_TELEGRAM_ID INTEGER,
REFERRAL_TELEGRAM_ID INTEGER,
UNIQUE(INVITER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
)
"""

INSERT_REFERENCE_QUERY = """
INSERT INTO reference VALUES(?,?,?)
"""