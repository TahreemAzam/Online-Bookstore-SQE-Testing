describe(' Book details capture test', () => {

  beforeEach(() => {
    cy.visit('https://sahup9156.github.io/bookworms/shop.html');
  });

  it('TC-14 - Add to cart', () => {

    // Click first available "Add to cart" button (ensures book exists)
    cy.contains('button', 'Add to cart')
      .first()
      .should('be.visible')
      .click();
  });

});
