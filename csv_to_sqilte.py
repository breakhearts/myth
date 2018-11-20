from app import db, VoteMessage
from datetime import datetime


def csv_to_sqlite(filename):
    with open(filename, "r") as f:
        f.readline()
        for _, line in enumerate(f):
            id, answer_start, answer_end, _, username, mobile, qq, grade, school, rank, book_type, book_pic_1, book_pic_2, book_design_pic, book_read_me, book_skill, selected = [x.strip('"') for x in line.split(",")]
            answer_start = datetime.strptime(answer_start, "%Y-%m-%d %H:%M:%S")
            answer_end = datetime.strptime(answer_end, "%Y-%m-%d %H:%M:%S")
            book_pic_1 = book_pic_1.split('"')[-3]
            if book_pic_2 != "":
                book_pic_2 = book_pic_2.split('"')[-3]
            book_design_pic = book_design_pic.split('"')[-3]
            print(id, answer_start, answer_end,  username, mobile, qq, grade, school, rank, book_type, book_pic_1, book_pic_2, book_design_pic,book_read_me, book_skill, selected)
            vm = VoteMessage(id=id, answer_start=answer_start, answer_end=answer_end, username=username, mobile=mobile,
                             qq=qq, grade=grade, school=school, rank=rank, book_type=book_type, book_pic_1=book_pic_1,
                             book_pic_2=book_pic_2,book_design_pic=book_design_pic,book_read_me=book_read_me,book_skill=book_skill)
            db.session.merge(vm)
    db.session.commit()

if __name__ == "__main__":
    csv_to_sqlite("1.csv")