import PyPDF2
import sys


class Schedule:
    def __init__(self, courseID, section, date, time, room):
        self.courseID = courseID
        self.section = section
        self.date = date
        self.time = time
        self.room = room

    def __str__(self):
        return (self.courseID + "\t"
                + self.section + "\t"
                + self.date + "\t"
                + self.time + "\t"
                + self.room + "\n"
                )



class ScheduleExtract:
    numPages = 36

    def readPage(self, pageNumber):
        pdfFile = open('../pdf/Exam_Schedule_171_revised.pdf', 'rb')
        reader = PyPDF2.PdfFileReader(pdfFile)

        pageObj = reader.getPage(pageNumber)
        dataObj = pageObj.extractText()

        pdfFile.close()

        data = dataObj.split('\n')

        return data

    def getSchedule(self, courseID, section):
        for pageNo in range(ScheduleExtract.numPages):
            dataFromPage = self.readPage(pageNo)

            for i in range(len(dataFromPage)):
                if courseID in dataFromPage[i] and dataFromPage[i + 1] == section:
                    schedule = Schedule(dataFromPage[i], dataFromPage[i + 1], dataFromPage[i + 2],
                                        dataFromPage[i + 3], dataFromPage[i + 4])

                    return schedule
                else:
                    continue


# main tasks here

extractor = ScheduleExtract()
courseFromCmd = sys.argv

scheduleAsList = []

for i in range(1, len(sys.argv), 2):
    sc = extractor.getSchedule(courseFromCmd[i], courseFromCmd[i + 1])
    print(sc)
    # writes schedule to a file
    scheduleAsList.append(str(sc))

print('\n')
writeToFile = input('Write schedule to file? [y/n]? ')
if writeToFile == 'y':
    outFile = open('../output/your_schedule.txt', 'w')
    outFile.close()

