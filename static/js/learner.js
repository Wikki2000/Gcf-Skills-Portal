import { ajaxRequest, inputColorFeedback } from './utils.js';

$(document).ready(function () {
  const inputId = 'code';
  const isValid = 'gcf_corpers';
  inputColorFeedback(inputId, isValid);


  $('#skills-form').submit(function (event) {
    event.preventDefault();

    const selectedSkills = [];

    // Retrieved a list of all checked box with it corresponding skills
    $('input[name="skills"]:checked').each(function () {
      selectedSkills.push($(this).val());
    });

    // Check if valid code is enter
    const code = $('#code').val()
    if (code !== isValid) {
      alert('Inavlid GCF ID. Try Again');
      return;
    }
    // Retrieved value from form field.
    const other_skills = $('#other-skills').val();
    const data = JSON.stringify({
      name: $('#name').val(),
      email: $('#email').val(),
      phone_number: $('#whatsapp').val(),
      skills: selectedSkills,
      other_skills: other_skills ? other_skills : 'None'
    });
    // Sent registration data to server to be process
    const url = 'http://127.0.0.1:5000/gcf/register-learner'
    ajaxRequest(url, 'POST', data,
      (response) => {
        if (response.status === 'Success') {
	  const sucessUrl = 'http://127.0.0.1:5000/gcf/register-success';
	  window.location.href = sucessUrl;
        }
      },
      (error) => {
        const failureUrl = 'http://127.0.0.1:5000/gcf/register-fail';
	window.location.href = failureUrl;
      }
    );
  });
});
