import { Link } from 'react-router-dom'

export default function Footer() {
  return (
    <footer className="bg-gray-900 text-gray-400 py-10 mt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-8">
          <div>
            <p className="text-white font-bold text-lg mb-2">🎟️ EventHub</p>
            <p className="text-sm">Discover and attend events near you.</p>
          </div>
          <nav aria-label="Footer navigation">
            <p className="text-white font-semibold mb-2 text-sm">Explore</p>
            <ul className="space-y-1 text-sm">
              <li><Link to="/events" className="hover:text-white transition-colors">Browse Events</Link></li>
              <li><Link to="/register" className="hover:text-white transition-colors">Create Account</Link></li>
            </ul>
          </nav>
          <div>
            <p className="text-white font-semibold mb-2 text-sm">Organizers</p>
            <ul className="space-y-1 text-sm">
              <li><Link to="/register" className="hover:text-white transition-colors">Host an Event</Link></li>
              <li><Link to="/dashboard" className="hover:text-white transition-colors">Dashboard</Link></li>
            </ul>
          </div>
        </div>
        <div className="mt-8 pt-6 border-t border-gray-800 text-sm text-center">
          © {new Date().getFullYear()} EventHub. Built for CMPE-202 Software Systems Engineering.
        </div>
      </div>
    </footer>
  )
}
