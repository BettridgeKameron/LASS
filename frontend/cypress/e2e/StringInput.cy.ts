describe('String Input Component', () => {
  it('successfully loads and interacts with StringInput component', () => {
    cy.visit('/');
    cy.get('input').type('hello');
    cy.get('button').click();
    cy.contains('Reversed String: olleh');
  });
});

