/**
 * Sends an AJAX request.
 *
 * @param {string} url - The URL to which the request is sent.
 * @param {string} method - The HTTP method to use for request.
 * @param {object} data - The data to send with the request. Default is an empty object.
 * @param {function} onSuccess - Callback function to execute if the request succeeds.
 * @param {function} onError - Callback function to execute if the request fails.
 */
export function ajaxRequest(url, method, data = {}, onSuccess, onError) {
  $.ajax({
    url: url,
    method: method,
    contentType: 'application/json',
    data: data,
    success: onSuccess,
    error: onError
  });
}

/**
 * Give visual feedback for inut validation.
 *
 * @param {string} inputId - The ID of the input field.
 * @param {string} isValid - The criteria to validate input.
 * @param {string} invalidColor - Display color for invalid input - Default is red
 * @param {string} validColor - Display color for for valid input - Default is white
 */
export function inputColorFeedback(inputId, isValid, invalidColor = 'red', validColor = 'white') {
  $(`#${inputId}`).on('input', function (event) {
    const inputValue = $(this).val();

    if (inputValue === isValid) {
      $(this).css('background-color', 'white');
    } else {
      event.preventDefault();
      $(this).css('background-color', '#ffcccc');
    }
  });
}
