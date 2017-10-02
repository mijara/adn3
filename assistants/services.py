def has_pretestupload(pretest, student):
    for pretestupload in pretest.pretestupload_set.all():
        if student == pretestupload.student.user:
            return pretestupload
    return None

def get_next_pretestupload(pretest, agenda, current):
    flag = False
    for pretestupload in pretest.pretestupload_set.all():
        if pretestupload.student.user in agenda.inscriptions.all() and (pretestupload == current or flag):
            if flag:
                return pretestupload
            flag = True
    return None