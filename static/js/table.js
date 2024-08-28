$(document).ready(function () {

  const trainerUrl = 'http://127.0.0.1:5000/gcf/trainers'; 
  const learnerUrl = 'http://127.0.0.1:5000/gcf/learners';

  // Retrieve trainers from database
  $.get(trainerUrl,
    (response) => {
      $.each(response, function (index, trainer) {
        const row = `<tr>
          <td>${index + 1}</td>
          <td>${trainer.name}</td>
          <td>${trainer.email}</td>
          <td>${trainer.contact}</td>
          <td>${trainer.skills}</td>
          <td>${trainer.create_at}</td>
        </tr>`;
        $('#trainers-table tbody').append(row);
      });
  }, 'json');

  // Retrieve learner from database
  $.get(learnerUrl,
    (response) => {
      $.each(response, function (index, learner) {
        const row = `<tr>
          <td>${index + 1}</td>
          <td>${learner.name}</td>
          <td>${learner.email}</td>
	  <td>${learner.contact}</td>
	  <td>${learner.skills}</td>
	  <td>${learner.create_at}</td>
	</tr>`;
        $('#learners-table tbody').append(row);
        console.log(row);
      });
    }, 'json');
});
