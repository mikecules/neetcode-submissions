from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = deque(students)
        sandwiches_queue = deque(sandwiches)

        while True:
            sandwiches_count = len(sandwiches_queue)
            if sandwiches_count == 0:
                break

            sandwich = sandwiches_queue.popleft()

            len_students = len(student_queue)
            students_examined_count = 0
            student_matched_with_sandwhich = False

            while students_examined_count < len_students:
                print(students_examined_count, student_queue)

                student = student_queue.popleft()
                if student != sandwich:
                    student_queue.append(student)
                else:
                    student_matched_with_sandwhich = True
                    break

                students_examined_count += 1

            if not student_matched_with_sandwhich:
                break

        return len(student_queue)
