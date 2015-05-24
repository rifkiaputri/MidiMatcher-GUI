import os
import searchmanager


def main():
    # Set input and output path
    # rawDBPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher_Swing/files/'
    dbPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher_Swing/transcriptions/'
    recordPath = 'D:/Data Kiki/Tugas/Tingkat 4/Tugas Akhir/MidiMatcher_Swing/records/'

    # Init database
    # print 'Initializing database...'
    controller = searchmanager.SearchManager()
    # controller.init(rawDBPath, dbPath)
    # print 'Database successfully initialized.'

    recordName = 'query'

    if os.path.isfile(recordPath + recordName + '.wav'):
        # Call praat script for humming transcription
        os.system('praatcon.exe pitch_listing.praat 10 yes 0 70 2000 \"' + recordName + '\"')

        # Begin searching module
        result = controller.getDistance(recordPath, recordName, dbPath)
        controller.sortByDist(result, 10, recordPath, recordName)
        print '\n'

    else:
        print 'No such file.'

if __name__ == '__main__':
    main()