from odoo import http
from odoo.http import request
from datetime import date, timedelta

class ReadingDashboard(http.Controller):

    @http.route('/reading_dashboard', type='http', auth='user', website=True)
    def reading_dashboard(self):
        today = date.today()
        start_date = today - timedelta(days=365)

        # Ambil data baca dalam 1 tahun terakhir
        records = request.env['book.reading.day'].sudo().search([
            ('date', '>=', start_date),
            ('date', '<=', today)
        ])

        read_dates = set(r.date.isoformat() for r in records)

        # Build grid data (7 x 53 weeks)
        grid = []
        for i in range(53):  # weeks
            col = []
            for j in range(7):  # days
                day = start_date + timedelta(days=(i * 7 + j))
                if day > today:
                    continue
                col.append({
                    'date': day,
                    'read': day.isoformat() in read_dates
                })
            grid.append(col)

        return request.render('book_reading_tracker.reading_dashboard_template', {
            'grid': grid
        })
