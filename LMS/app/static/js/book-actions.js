// Book Borrowing
document.addEventListener('DOMContentLoaded', () => {
    const borrowButtons = document.querySelectorAll('.borrow-button');

    borrowButtons.forEach(button => {
        button.addEventListener('click', async (e) => {
            e.preventDefault();
            const bookId = button.dataset.bookId;

            try {
                const response = await fetch(`/borrow/${bookId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });

                if (response.ok) {
                    alert('Book borrowed successfully!');
                    window.location.reload();
                } else {
                    alert('Failed to borrow book. Please try again.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    });
});

// Feedback Submission
document.addEventListener('DOMContentLoaded', () => {
    const feedbackForm = document.querySelector('#feedback-form');

    if (feedbackForm) {
        feedbackForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(feedbackForm);

            try {
                const response = await fetch('/add_feedback', {
                    method: 'POST',
                    body: formData,
                });

                if (response.ok) {
                    alert('Feedback submitted successfully!');
                    window.location.reload();
                } else {
                    alert('Failed to submit feedback. Please try again.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }
});