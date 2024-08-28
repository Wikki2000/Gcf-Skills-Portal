import { ajaxRequest } from './utils.js';

$(document).ready(function () {
  $('#cancel').click(function () {
    window.location.href = 'http://127.0.0.1:5000/gcf/register-learner';
  });

  $('#trainer-form').on('submit', function (event) {
    event.preventDefault();

    // Retrieved value from form field.
    const data = JSON.stringify({
      name: $('#name').val(),
      email: $('#email').val(),
      phone_number: $('#whatsapp').val(),
      skills: $("#skills").val()
    });

    // Sent registration data to server to be process
    const url = 'http://127.0.0.1:5000/gcf/register-trainer';
    ajaxRequest(url, 'POST', data,
      (response) => {
        if (response.status === 'Success') {
	  const successUrl = 'http://127.0.0.1:5000/gcf/register-success';
	  window.location.href = successUrl;
        }
      },
      (error) => {
	const failureUrl = 'http://127.0.0.1:5000/gcf/register-fail';
	window.location.href = failureUrl;
      }
    );
  });
});
