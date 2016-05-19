import sys
import re
from collections import Counter


class ParseIpCommand:
    """
    Simple command to parse IP from the file
    and print top 10 most frequently logged IP
    from that file
    """
    default_ip_regex = re.compile(
        r'((?:[0-9]{1,3}\.){3}[0-9]{1,3})',
        re.MULTILINE
    )

    def __init__(self,
                 file_path,
                 ip_regex=None):
        self.file_path = file_path
        self.ip_regex = (
            ip_regex or
            self.default_ip_regex
        )

    def get_ip_list(self, data):
        """
        Finds all the ip address in the data and returns a list
        """
        return self.ip_regex.findall(data)

    def get_ip_summary(self, ip_list):
        """
        Creates a summary of ip_list
        Key will be ip address and the value will be the count
        eg:
        {
            '52.86.190.192': 14
        }
        """
        counter_dict = Counter()
        for ip in ip_list:
            counter_dict[ip] += 1
        return counter_dict

    def sort_summary(self, ip_summary):
        """
        Sorts the summary dict in assending order
        """
        return sorted(
            ip_summary.items(),
            key=lambda value: value[1],
            reverse=True
        )

    def print_top_ten(self, sorted_summary):
        """
        Prints the top 10 ip address from the summary
        """
        for val in sorted_summary[:10]:
            print('%s - %s' % (val[0], val[1]))

    def run(self):
        file = open(self.file_path, 'r')
        data = file.read()
        ip_list = self.get_ip_list(data)
        ip_summary = self.get_ip_summary(ip_list)
        sorted_summary = self.sort_summary(ip_summary)
        self.print_top_ten(sorted_summary)
        file.close()


if __name__ == '__main__':
    file_path = sys.argv[1]
    ParseIpCommand(file_path=file_path).run()
