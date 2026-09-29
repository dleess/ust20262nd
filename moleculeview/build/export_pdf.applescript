on run argv
    set sourcePath to item 1 of argv
    set outputPath to item 2 of argv
    with timeout of 180 seconds
        tell application "Microsoft PowerPoint"
            open (POSIX file sourcePath)
            set lecturePresentation to active presentation
            save lecturePresentation in (POSIX file outputPath) as save as PDF
            close lecturePresentation saving no
        end tell
    end timeout
end run
