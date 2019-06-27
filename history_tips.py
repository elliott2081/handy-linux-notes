#
historylinks =  {
    "LH History Tips": "https://lifehacker.com/review-your-most-oft-used-unix-commands-202712",
    "LH Unix Most Used Commans": "https://lifehacker.com/review-your-most-oft-used-unix-commands-202712",
    "L3": "na"
}

print(historylinks)
LH = "Terminal power users already know that a log of all the commands you execute are kept in history. (Go ahead, type history to see them.) Last week we saw that you can sudo your previous command using the !! (bang-bang) notation. Well, you can also search your command history as you type using the very useful Ctrl+R key combination. Give it a try: in the terminal, hold down Ctrl and press R to invoke reverse-i-search. Type a letter - like s - and you'll get a match for the most recent command in your history that starts with s. Keep typing to narrow your match. When you hit the jackpot, press Enter to execute the suggested command. Also, !characters will execute the last command that matches the specified characters. (So !ssh will run the last ssh you used.) \n Of course good history search only works if you've got a long history. To extend the length of the history list in your terminal, add the following lines to your .bash_profile: \n\n HISTFILESIZE=1000000000 \n HISTSIZE=1000000 \n Once you've got your history built up, you can use this command to see what items you type in the terminal the most. (Great way to decide what aliases you need to set up.)"

LH2 = """
IBM author Michael Stutz lists several ways UNIX users can benchmark and increase their productivity at the command line. One is to use the built in history tool to review what programs you use the most, using this command:

    history|awk '{print $2}'|awk 'BEGIN {FS="|"} {print $1}'|sort|uniq -c|sort -r

    The result will be a list of commands you've issued ordered by frequency. This is a fabulous way to identify what commands could use a shorter alias; for example, if I type ssh mylongservername.com 20 times a day, it's worth setting up an alias like sshg to get that done in fewer keystrokes.
"""
print("\n --------- Article 1 -------- ")
print(LH)
print("\n --------- Article 2 -------- ")
print(LH2)
