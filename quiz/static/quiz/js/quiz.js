let quiz = document.getElementById('quiz');
var askQuestion = document.getElementById("askQuestion");
var form = document.getElementById("form");
let submitBtn = document.getElementById('submitBtn');
var displayScore = document.getElementById("displayScore");
var displayQCount = document.getElementById("displayQCount"); 
var displayQMCount = document.getElementById("displayQMCount"); 
const questionCard = document.querySelector("#quiz-section");
const startBtn = document.querySelector("#start-button");

// questions array
var questions = [
  {
    question: "Question 1",
    choices: ["A", "B", "C", "D", "E", "F"],
    correct: 1
  },
  {
    question: "Question 2",
    choices: ["A", "B", "C", "D"],
    correct: 1
  }
]; 

document.querySelector("#start-button").addEventListener("click", startQuiz);

function startQuiz() {
    //show the question card
    questionCard.removeAttribute("hidden");
    startBtn.style.visibility = 'hidden'
}

window.onload = beginQuiz;
function beginQuiz() {
  quiz.style.display = "block";
  showScore.style.display = "none";
  i = 0;
  score = 0;
  questionsCount = questions.length;
  answersCount = questions[i].choices.length;
  displayQCount.innerHTML = 1;
  displayQMCount.innerHTML = questionsCount;
  displayScore.innerHTML = 0;
  getQAs();
}

// listen and do things when the button is clicked
submitBtn.addEventListener("click", function() {
  allRadios = document.getElementsByName("option");
  var isChecked = false;
  for (var j = 0; j < allRadios.length; j++) {
    if (allRadios[j].checked) {
      isChecked = true;
      checkedRadio = j;
      break;
    }
  } 
  if (!(isChecked)) {
    alert("Please select an answer before moving on");
  } else {
    getResults();
    deselectRadios();
    i++;
    displayQCount.innerHTML = i + 1;
    getQAs();
  }
});

function deselectRadios() {
  allRadios = document.getElementsByName("option");
  for (var p = 0; p < allRadios.length; p++) {
    allRadios[p].checked = false;
  }
}

function getResults() {
  if (allRadios[checkedRadio].value === questions[i].choices[questions[i].correct]) {
    score++;
    displayScore.innerHTML = score;
  }
}

function getQAs() {
  if (i < questionsCount) {
    askQuestion.innerHTML = questions[i].question; // populate question text
    for (var k = 0; k < answersCount; k++) {
      document.getElementById("answer" + k).innerHTML = questions[i].choices[k];
      document.getElementById("answer" + k).setAttribute("for", questions[i].choices[k]); // set the for
      document.getElementById("label" + k).setAttribute("value", questions[i].choices[k]); // set the value
    }
  } else {
    displayResults();
  }
};

function displayResults() {
  quiz.style.display = "none";
  showScore.style.display = "block";
  inform.innerHTML = "Your recommended products are:";
};

resetBtn.addEventListener("click", function() {
  beginQuiz();
});