class workout_section {
    constructor(section_num) {
        var sectionDiv = document.createElement("div");
        sectionDiv.className = "row mb-3"
        sectionDiv.id = "section".concat(section_num)
        var section_h3 = document.createElement("h3")
        var h3_text = document.createTextNode("Section ".concat(section_num))
        section_h3.appendChild(h3_text)
        sectionDiv.appendChild(section_h3)
    }

}


function add_section() {
    // get the form from the HTML page
    // eventually workout is it's own section with id=workoutcontent
    // then you get the sectionid for wherever the button was pressed
//    var curr_section = document.getElementById("section1");
    //new h2 section #
    //new num rounds
    // new scored checkbox
    //new exercise 1 and reps 1

    var curr_section = document.getElementById("workout_content");

    var sectionDiv = document.createElement("div");
    sectionDiv.className = "row mb-3";
    sectionDiv.id = "section".concat("2");

    var h3_row = document.createElement("div");
    h3_row.className = "row";
    var section_h3 = document.createElement("h3");
    var h3_text = document.createTextNode("Section ".concat("2"));
    section_h3.appendChild(h3_text);
    h3_row.appendChild(section_h3);
    sectionDiv.appendChild(h3_row);

    var new_row = document.createElement("div");
    new_row.className = "row mb-3 align-items-center";
    var num_rounds_col = document.createElement("div");
    num_rounds_col.className = "col-sm";
    var num_rounds_col_label = document.createElement("Label");
    num_rounds_col_label.setAttribute("for", "num_rounds".concat("2"));
    num_rounds_col_label.className = "form-label";
    num_rounds_col_label.innerHTML = "Num Rounds";
    num_rounds_col.appendChild(num_rounds_col_label);
    var num_rounds_input = document.createElement("input");
    num_rounds_input.type = "text";
    num_rounds_input.className = "form-control";
    num_rounds_input.setAttribute("id", "num_rounds".concat("2"));
    num_rounds_input.setAttribute("name", "num_rounds".concat("2"));
    num_rounds_input.setAttribute("value", "");
    num_rounds_col.appendChild(num_rounds_input);
    new_row.appendChild(num_rounds_col);

    var form_checkbox_col = document.createElement("div");
    form_checkbox_col.className = "col-sm";
    var form_check = document.createElement("div");
    form_check.className = "form-check";
    var scored_checkbox_input = document.createElement("input");
    scored_checkbox_input.className = "form-check-input"
    scored_checkbox_input.setAttribute("id", "scored_checkbox_".concat("2"));
    scored_checkbox_input.setAttribute("name", "scored_checkbox_".concat("2"));
    scored_checkbox_input.setAttribute("type", "checkbox");
    scored_checkbox_input.setAttribute("value", "y");
    form_check.appendChild(scored_checkbox_input);
    var scored_checkbox_label = document.createElement("Label");
    scored_checkbox_label.setAttribute("for", "scored_checkbox_".concat("2"));
    scored_checkbox_label.className = "form-check-label";
    scored_checkbox_label.innerHTML = "Scored";
    form_check.appendChild(scored_checkbox_label);
    form_checkbox_col.appendChild(form_check);
    new_row.appendChild(form_checkbox_col);

    var new_row2 = document.createElement("div");
    new_row2.className = "row mb-3";
    var exercise_col = document.createElement("div");
    exercise_col.className = "col-sm";
    var exercise_label = document.createElement("Label");
    exercise_label.setAttribute("for", "exercise".concat("2"));
    exercise_label.className = "form-label";
    exercise_label.innerHTML = "Exercise";
    exercise_col.appendChild(exercise_label);
    var exercise_input = document.createElement("input");
    exercise_input.type = "text";
    exercise_input.className = "form-control";
    exercise_input.setAttribute("id", "num_rounds".concat("2"));
    exercise_input.setAttribute("name", "num_rounds".concat("2"));
    exercise_input.setAttribute("value", "");
    exercise_col.appendChild(exercise_input);
    new_row2.appendChild(exercise_col);

    var num_sets_col = document.createElement("div");
    num_sets_col.className = "col-sm";
    var num_sets_label = document.createElement("Label");
    num_sets_label.setAttribute("for", "num_sets".concat("2"));
    num_sets_label.className = "form-label";
    num_sets_label.innerHTML = "Sets";
    num_sets_col.appendChild(num_sets_label);
    var num_sets_input = document.createElement("input");
    num_sets_input.type = "text";
    num_sets_input.className = "form-control";
    num_sets_input.setAttribute("id", "num_sets".concat("2"));
    num_sets_input.setAttribute("name", "num_sets".concat("2"));
    num_sets_input.setAttribute("value", "");
    num_sets_col.appendChild(num_sets_input);
    new_row2.appendChild(num_sets_col);

    var num_reps_col = document.createElement("div");
    num_reps_col.className = "col-sm";
    var num_reps_label = document.createElement("Label");
    num_reps_label.setAttribute("for", "num_reps".concat("2"));
    num_reps_label.className = "form-label";
    num_reps_label.innerHTML = "Reps";
    num_reps_col.appendChild(num_reps_label);
    var num_reps_input = document.createElement("input");
    num_reps_input.type = "text";
    num_reps_input.className = "form-control";
    num_reps_input.setAttribute("id", "num_reps".concat("2"));
    num_reps_input.setAttribute("name", "num_reps".concat("2"));
    num_reps_input.setAttribute("value", "");
    num_reps_col.appendChild(num_reps_input);
    new_row2.appendChild(num_reps_col);

    var new_row3 = document.createElement("div");
    new_row3.className = "row mb-3";
    var add_section_col = document.createElement("div");
    add_section_col.className = "col-sm";
    var add_section_button = document.createElement("BUTTON");
    add_section_button.innerHTML = "Add Section";
    add_section_button.className = "btn btn-outline-dark";
    add_section_button.setAttribute("id", "addSectionButton".concat("2"));
    add_section_button.setAttribute("name", "add_section_button".concat("2"));
    add_section_button.setAttribute("onclick", "add_section()");
    add_section_button.setAttribute("type", "button");
    add_section_button.setAttribute("value", "");
    add_section_col.appendChild(add_section_button);
    new_row3.appendChild(add_section_col);
    var add_exercise_col = document.createElement("div");
    add_exercise_col.className = "col-sm";
    var add_exercise_button = document.createElement("BUTTON");
    add_exercise_button.innerHTML = "Add Exercise";
    add_exercise_button.className = "btn btn-outline-primary";
    add_exercise_button.setAttribute("id", "addExerciseButton".concat("2"));
    add_exercise_button.setAttribute("name", "add_exercise_button".concat("2"));
    add_exercise_button.setAttribute("onclick", "add_exercise()");
    add_exercise_button.setAttribute("type", "button");
    add_exercise_button.setAttribute("value", "");
    add_exercise_col.appendChild(add_exercise_button);
    new_row3.appendChild(add_exercise_col);

    sectionDiv.appendChild(new_row);
    sectionDiv.appendChild(new_row2);
    sectionDiv.appendChild(new_row3);

    curr_section.appendChild(sectionDiv);

//<div class="row mb-3" id="section1">
//  <div class="row">
//    <h3>Section 1</h3>
//  </div>
//  <div class="row align-items-center">
//    <div class="col-sm">
//      {{ form.num_rounds.label(class="form_label") }}
//      {{ form.num_rounds(class="form-control") }}
//    </div>
//    <div class="col-sm">
//      <div class="form-check">
//        {{ form.scored_checkbox(class="form-check-input") }}
//        {{ form.scored_checkbox.label(class="form-check-label") }}
//      </div>
//    </div>
//  </div>
//  <div class="col-sm">
//    {{ form.exercise1.label(class="form-label") }}
//    {{ form.exercise1(class="form-control") }}
//  </div>
//  <div class="col-sm">
//    {{ form.num_sets1.label(class="form-label") }}
//    {{ form.num_sets1(class="form-control") }}
//  </div>
//  <div class="col-sm">
//    {{ form.num_reps1.label(class="form-label") }}
//    {{ form.num_reps1(class="form-control") }}
//  </div>
//</div>


    //var form_elems = form.childNodes

    //addsection# button automatically knows what ID to give the next section
    //add exercise will be inside the section
    //need to know where to add new section based on section button ID (add function parameter?)

}

//function add_exercise() {
//
//}
//
//// Create an input element for Full Name
//var FN = document.createElement("input");
//FN.setAttribute("type", "text");
//FN.setAttribute("name", "FullName");
//FN.setAttribute("placeholder", "Full Name");
//
//// Create an input element for date of birth
//var DOB = document.createElement("input");
//DOB.setAttribute("type", "text");
//DOB.setAttribute("name", "dob");
//DOB.setAttribute("placeholder", "DOB");
//
//// Create an input element for emailID
//var EID = document.createElement("input");
//EID.setAttribute("type", "text");
//EID.setAttribute("name", "emailID");
//EID.setAttribute("placeholder", "E-Mail ID");
//
//// Create an input element for password
//var PWD = document.createElement("input");
//PWD.setAttribute("type", "password");
//PWD.setAttribute("name", "password");
//PWD.setAttribute("placeholder", "Password");
//
//// Create an input element for retype-password
//var RPWD = document.createElement("input");
//RPWD.setAttribute("type", "password");
//RPWD.setAttribute("name", "reTypePassword");
//RPWD.setAttribute("placeholder", "ReEnter Password");
//
//// create a submit button
//var s = document.createElement("input");
//s.setAttribute("type", "submit");
//s.setAttribute("value", "Submit");
//
//// Append the full name input to the form
//form.appendChild(FN);
//
//// Inserting a line break
//form.appendChild(br.cloneNode());
//
//// Append the DOB to the form
//form.appendChild(DOB);
//form.appendChild(br.cloneNode());
//
//// Append the emailID to the form
//form.appendChild(EID);
//form.appendChild(br.cloneNode());
//
//// Append the Password to the form
//form.appendChild(PWD);
//form.appendChild(br.cloneNode());
//
//// Append the ReEnterPassword to the form
//form.appendChild(RPWD);
//form.appendChild(br.cloneNode());
//
//// Append the submit button to the form
//form.appendChild(s);
//
//document.getElementsByTagName("body")[0]
//.appendChild(form);
//}