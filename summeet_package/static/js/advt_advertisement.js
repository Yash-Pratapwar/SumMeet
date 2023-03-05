// After form loads focus will go to Company name field.
function firstfocus() {
    var meeting_namef = document.advertisements.meeting_name.focus();
    return true;
}
function validate() {
    var meeting_name = document.advertisements.meeting_name.value;
    var meeting_namef = document.advertisements.meeting_name;
    var meeting_date = document.advertisements.meeting_date.value;
    var meeting_datef = document.advertisements.meeting_date;
    var meeting_agenda = document.advertisements.meeting_agenda.value;
    var meeting_agendaf = document.advertisements.meeting_agenda;
    var mailing_list = document.advertisements.mailing_list.value;
    var mailing_listf = document.advertisements.mailing_list.value;
    var mailing_listf = document.advertisements.mailing_list;
    var mtng_file = document.advertisements.mtng_file.value;
    var mtng_filef = document.advertisements.mtng_file;
    

    if (meeting_name == "" || meeting_name == null) {
        alert("Please enter meeting date and time.");
        meeting_namef.focus();
        return false;
    }

    else if (meeting_date == "" || meeting_date == null) {
        alert("Please enter meeting date and time.");
        meeting_datef.focus();
        return false;
    }

    else if (meeting_agenda == "" || meeting_agenda == null) {
        alert("Please enter meeting agenda.");
        meeting_agendaf.focus();
        return false;
    }

    else if (mailing_list == "" || mailing_list == null) {
        alert("Please enter receipients.");
        meeting_agendaf.focus();
        return false;
    }

    // else if ($('#emailsList ul').length == 0) {
    //     alert("Please enter receipients.");
    //     mailing_listf.focus();
    //     return false;
    // }

    else if (mtng_file == "" || mtng_file == null) {
        alert("Please upload a valid file (mp3/mp4/wav).");
        mtng_filef.focus();
        return false;
    }    
}

