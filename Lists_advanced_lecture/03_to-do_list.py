notes = [num for num in range(0, 11)]
notes_normal = [num for num in range(0,11)]
while True:
    to_do_notes = input().split('-')
    if to_do_notes[0] == 'End':
        break

    else:
        importance = int(to_do_notes[0])
        activity = to_do_notes[1]
        if importance in notes:
            notes[importance] = activity

        # for impor in notes:#maybe forcycle
        #     if impor == importance:
        #         notes[impor] = activity
notes = [act for act in notes if not act in notes_normal]
print(notes)